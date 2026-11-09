"""Ollama workers selected at request boundaries for optional multi-host inference."""

import os
import threading
import time
from dataclasses import dataclass, field
from urllib.parse import urlparse

import requests


VARSAYILAN_OLLAMA_HOSTU = "http://localhost:11434"


class OllamaHavuzYapilandirmaHatasi(ValueError):
    """A host-pool environment setting is invalid."""


class OllamaCalisanKullanilamiyor(RuntimeError):
    """No configured Ollama worker can serve a request."""


@dataclass
class _OllamaCalisani:
    taban_url: str
    modeller: set = field(default_factory=set)
    son_hata: str = ""
    son_basarisizlik_zamani: float = 0.0


def _pozitif_tamsayi_ortam_degeri(ad: str, varsayilan: int) -> int:
    deger = os.getenv(ad, "").strip()
    if not deger:
        return varsayilan
    try:
        sonuc = int(deger)
    except ValueError as hata:
        raise OllamaHavuzYapilandirmaHatasi(f"{ad} pozitif bir tam sayı olmalıdır.") from hata
    if sonuc <= 0:
        raise OllamaHavuzYapilandirmaHatasi(f"{ad} pozitif bir tam sayı olmalıdır.")
    return sonuc


def _hostu_normallestir(host: str) -> str:
    sonuc = host.strip().rstrip("/")
    ayrik = urlparse(sonuc)
    if ayrik.scheme not in ("http", "https") or not ayrik.netloc or ayrik.username or ayrik.password:
        raise OllamaHavuzYapilandirmaHatasi(
            f"Geçersiz Ollama hostu: {host!r}. http://sunucu:11434 biçimini kullanın."
        )
    if ayrik.path not in ("", "/") or ayrik.params or ayrik.query or ayrik.fragment:
        raise OllamaHavuzYapilandirmaHatasi(
            f"Ollama hostu yol, sorgu veya parça içeremez: {host!r}."
        )
    return sonuc


class OllamaHostHavuzu:
    """Model-aware, round-robin routing across complete Ollama model replicas."""

    def __init__(self, hostlar, baglanti_zaman_asimi=10, okuma_zaman_asimi=180):
        if not hostlar:
            raise OllamaHavuzYapilandirmaHatasi("En az bir Ollama hostu gereklidir.")
        temiz_hostlar = []
        for host in hostlar:
            temiz = _hostu_normallestir(host)
            if temiz not in temiz_hostlar:
                temiz_hostlar.append(temiz)
        self._calisanlar = [_OllamaCalisani(host) for host in temiz_hostlar]
        self.baglanti_zaman_asimi = baglanti_zaman_asimi
        self.okuma_zaman_asimi = okuma_zaman_asimi
        self._kilit = threading.Lock()
        self._sonraki_indeks = 0

    @classmethod
    def ortamdan_olustur(cls):
        ham_hostlar = os.getenv("ALTAR_OLLAMA_HOSTS", "").strip()
        hostlar = [h for h in ham_hostlar.split(",") if h.strip()] if ham_hostlar else [VARSAYILAN_OLLAMA_HOSTU]
        return cls(
            hostlar,
            baglanti_zaman_asimi=_pozitif_tamsayi_ortam_degeri("ALTAR_OLLAMA_CONNECT_TIMEOUT", 10),
            okuma_zaman_asimi=_pozitif_tamsayi_ortam_degeri("ALTAR_OLLAMA_READ_TIMEOUT", 180),
        )

    @property
    def hostlar(self):
        return [calisan.taban_url for calisan in self._calisanlar]

    @property
    def coklu_host_aktif_mi(self):
        return len(self._calisanlar) > 1 or self.hostlar != [VARSAYILAN_OLLAMA_HOSTU]

    def modelleri_yenile(self):
        """Probe every configured worker and return the union of its installed models."""
        tum_modeller = []
        for calisan in self._calisanlar:
            try:
                yanit = requests.get(
                    f"{calisan.taban_url}/api/tags",
                    timeout=(self.baglanti_zaman_asimi, self.baglanti_zaman_asimi),
                )
                yanit.raise_for_status()
                model_adlari = []
                for model in yanit.json().get("models", []):
                    if not isinstance(model, dict):
                        continue
                    model_adi = str(model.get("model") or model.get("name") or "").strip()
                    if model_adi and model_adi not in model_adlari:
                        model_adlari.append(model_adi)
                with self._kilit:
                    calisan.modeller = set(model_adlari)
                    calisan.son_hata = ""
                    calisan.son_basarisizlik_zamani = 0.0
                for model in model_adlari:
                    if model not in tum_modeller:
                        tum_modeller.append(model)
            except (requests.RequestException, ValueError) as hata:
                self._calisani_basarisiz_isaretle(calisan, hata)
        return tum_modeller

    def post(self, yol: str, *, model_adi=None, **kwargs):
        return self._istek("post", yol, model_adi=model_adi, **kwargs)

    def get(self, yol: str, *, model_adi=None, **kwargs):
        return self._istek("get", yol, model_adi=model_adi, **kwargs)

    def _istek(self, metot: str, yol: str, *, model_adi=None, **kwargs):
        zaman_asimi = kwargs.pop("timeout", (self.baglanti_zaman_asimi, self.okuma_zaman_asimi))
        calisanlar = self._uygun_calisanlari_sec(model_adi)
        hatalar = []
        for calisan in calisanlar:
            try:
                yanit = getattr(requests, metot)(f"{calisan.taban_url}{yol}", timeout=zaman_asimi, **kwargs)
            except requests.RequestException as hata:
                self._calisani_basarisiz_isaretle(calisan, hata)
                hatalar.append(f"{calisan.taban_url}: {hata}")
                continue

            if yanit.status_code in (502, 503, 504):
                yanit.close()
                hata = f"HTTP {yanit.status_code}"
                self._calisani_basarisiz_isaretle(calisan, hata)
                hatalar.append(f"{calisan.taban_url}: {hata}")
                continue
            return yanit

        model_bilgi = f" model '{model_adi}' için" if model_adi else ""
        ayrinti = "; ".join(hatalar) or "uygun veya sağlıklı host bulunamadı"
        raise OllamaCalisanKullanilamiyor(f"Ollama worker{model_bilgi} kullanılamıyor: {ayrinti}")

    def _uygun_calisanlari_sec(self, model_adi):
        with self._kilit:
            model_bulunan_calisanlar = [
                calisan for calisan in self._calisanlar
                if not model_adi or not calisan.modeller or model_adi in calisan.modeller
            ]
            if model_adi and all(calisan.modeller for calisan in self._calisanlar) and not model_bulunan_calisanlar:
                raise OllamaCalisanKullanilamiyor(
                    f"Hiçbir yapılandırılmış Ollama worker model '{model_adi}' içermiyor."
                )
            saglikli = [
                calisan for calisan in model_bulunan_calisanlar
                if (
                    (not calisan.son_hata or time.monotonic() - calisan.son_basarisizlik_zamani >= 30)
                )
            ]
            adaylar = saglikli or model_bulunan_calisanlar
            if not adaylar:
                adaylar = list(self._calisanlar)
            baslangic = self._sonraki_indeks % len(adaylar)
            self._sonraki_indeks += 1
            return adaylar[baslangic:] + adaylar[:baslangic]

    def _calisani_basarisiz_isaretle(self, calisan, hata):
        with self._kilit:
            calisan.son_hata = str(hata)
            calisan.son_basarisizlik_zamani = time.monotonic()


class OllamaHavuzIstemicisi:
    """Small ollama.Client-compatible adapter used by the agentic core."""

    def __init__(self, havuz: OllamaHostHavuzu):
        self.havuz = havuz

    def generate(self, *, model, prompt, **kwargs):
        yuk = {"model": model, "prompt": prompt, **kwargs}
        yanit = self.havuz.post("/api/generate", model_adi=model, json=yuk)
        yanit.raise_for_status()
        return yanit.json()
