import unittest
from unittest.mock import patch

import requests

from altar_ollama_havuzu import OllamaCalisanKullanilamiyor, OllamaHostHavuzu
from altar_zeka_cekirdegi import AltarAgenticCore


class _Yanit:
    def __init__(self, status_code=200, veri=None):
        self.status_code = status_code
        self._veri = veri or {}
        self.kapatildi = False

    def json(self):
        return self._veri

    def raise_for_status(self):
        if self.status_code >= 400:
            raise requests.HTTPError(f"HTTP {self.status_code}")

    def close(self):
        self.kapatildi = True


class OllamaHostHavuzuTestleri(unittest.TestCase):
    def test_modelleri_tum_worker_lardan_birlestirir(self):
        havuz = OllamaHostHavuzu(["http://gpu-a:11434", "http://gpu-b:11434"])
        with patch("altar_ollama_havuzu.requests.get") as get_istegi:
            get_istegi.side_effect = [
                _Yanit(veri={"models": [{"model": "qwen:latest"}]}),
                _Yanit(veri={"models": [{"model": "llama:latest"}]}),
            ]
            self.assertEqual(havuz.modelleri_yenile(), ["qwen:latest", "llama:latest"])

    def test_baglanti_hatasinda_sonraki_worker_a_gecer(self):
        havuz = OllamaHostHavuzu(["http://gpu-a:11434", "http://gpu-b:11434"])
        with patch("altar_ollama_havuzu.requests.post") as post_istegi:
            post_istegi.side_effect = [requests.ConnectionError("bağlantı reddedildi"), _Yanit()]
            yanit = havuz.post("/api/generate", model_adi="qwen:latest", json={"model": "qwen:latest"})

        self.assertEqual(yanit.status_code, 200)
        self.assertIn("http://gpu-a:11434/api/generate", post_istegi.call_args_list[0].args)
        self.assertIn("http://gpu-b:11434/api/generate", post_istegi.call_args_list[1].args)

    def test_istenen_modelin_oldugu_worker_i_secer(self):
        havuz = OllamaHostHavuzu(["http://gpu-a:11434", "http://gpu-b:11434"])
        with patch("altar_ollama_havuzu.requests.get") as get_istegi:
            get_istegi.side_effect = [
                _Yanit(veri={"models": [{"model": "qwen:latest"}]}),
                _Yanit(veri={"models": [{"model": "llama:latest"}]}),
            ]
            havuz.modelleri_yenile()

        with patch("altar_ollama_havuzu.requests.post", return_value=_Yanit()) as post_istegi:
            havuz.post("/api/chat", model_adi="llama:latest", json={"model": "llama:latest"})

        self.assertIn("http://gpu-b:11434/api/chat", post_istegi.call_args.args)

    def test_yuklu_olmayan_model_icin_acik_hata_verir(self):
        havuz = OllamaHostHavuzu(["http://gpu-a:11434"])
        with patch("altar_ollama_havuzu.requests.get", return_value=_Yanit(veri={"models": [{"model": "qwen:latest"}]})):
            havuz.modelleri_yenile()

        with self.assertRaisesRegex(OllamaCalisanKullanilamiyor, "içermiyor"):
            havuz.post("/api/chat", model_adi="llama:latest", json={"model": "llama:latest"})

    def test_otonom_ajan_havuz_istemcisini_kullanir(self):
        class _HavuzIstemcisi:
            havuz = object()

            def __init__(self):
                self.cagri = None

            def generate(self, **kwargs):
                self.cagri = kwargs
                return {"response": "4"}

        istemci = _HavuzIstemcisi()
        ajan = AltarAgenticCore(ollama_client=istemci)
        with patch("altar_zeka_cekirdegi.requests.post") as yerel_istek:
            sonuc = ajan._generate_guvenli("qwen:latest", "2 + 2 nedir?", {"num_ctx": 8192})

        self.assertEqual(sonuc, "4")
        self.assertFalse(yerel_istek.called)
        self.assertEqual(istemci.cagri["options"]["num_ctx"], 4096)


if __name__ == "__main__":
    unittest.main()
