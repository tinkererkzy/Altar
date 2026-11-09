import gc
import re
import ast
import json
import threading
import requests
import ollama

_RE_PYTHON_BLOCK = re.compile(r'```python\s*(.*?)```', re.DOTALL | re.IGNORECASE)
_RE_JSON_OBJ = re.compile(r'\{.*\}', re.DOTALL)
_RE_THOUGHT_TAGS = re.compile(
    r'<(think|düşünce|thought|durum_analizi|kural_denetimi)>.*?</\1>|'
    r'<think>.*?$|'
    r'^\s*(?:Thinking Process|Düşünme Süreci|Thought Process):.*?(?:\n\s*\n\s*(?=[A-ZÇĞİÖŞÜa-zçğıöşü])|\Z)',
    re.DOTALL | re.IGNORECASE | re.MULTILINE
)


class AltarAgenticCore:
    """
    %100 Bellek-İçi (In-Memory) ve Salt-Okunur (Read-Only) çalışan İleri Düzey Otonom Zekâ Çekirdeği.
    Özellikler: Re-Ranking, Sıkıştırma, Düşünce Ağacı, Dinamik Parametre/Derinlik,
    AST Hata Düzeltici, Mantıksal Kural Denetleyicisi (Critic) ve Halüsinasyon Dedektörü.
    """

    def __init__(self, ollama_client=None, aktif_kontrol_cb=None, dis_kilit=None):
        self.client = ollama_client if ollama_client else ollama.Client(host='http://localhost:11434')
        self.sabit_ctx = 4096  # 16 GB RAM'de 0xC0000005 bellek taşmasını önleyen güvenli KV-Cache sınırı
        self.aktif_kontrol_cb = aktif_kontrol_cb
        self._kilit = dis_kilit if dis_kilit is not None else threading.Lock()

    def _devam_edebilir_mi(self) -> bool:
        if callable(self.aktif_kontrol_cb):
            try:
                return bool(self.aktif_kontrol_cb())
            except Exception:
                return True
        return True

    def _generate_guvenli(self, model_adi: str, prompt: str, options: dict, json_modu: bool = False) -> str:
        """Ollama generate çağrılarını thread-safe kilit altında, think=False ile ve bellek taşmasına karşı korumalı yürütür."""
        if not self._devam_edebilir_mi():
            return ""
        opts = dict(options or {})
        opts["num_ctx"] = min(int(opts.get("num_ctx", self.sabit_ctx)), 4096)

        payload = {
            "model": model_adi,
            "prompt": prompt,
            "stream": False,
            "think": False,
            "options": opts
        }
        if json_modu:
            payload["format"] = "json"

        ham = ""
        with self._kilit:
            if getattr(self.client, "havuz", None) is not None:
                ek_parametreler = {"options": opts, "think": False}
                if json_modu:
                    ek_parametreler["format"] = "json"
                yanit = self.client.generate(model=model_adi, prompt=prompt, **ek_parametreler)
                ham = yanit.get("response", "") if isinstance(yanit, dict) else getattr(yanit, "response", "")
                if not ham and isinstance(yanit, dict) and yanit.get("thinking", ""):
                    ham = _RE_THOUGHT_TAGS.sub("", yanit["thinking"]).strip()
                return _RE_THOUGHT_TAGS.sub("", ham).strip()

            try:
                resp = requests.post("http://localhost:11434/api/generate", json=payload, timeout=120)
                if resp.status_code == 200:
                    veri = resp.json()
                    ham = veri.get("response", "")
                    if not ham and veri.get("thinking", ""):
                        ham = _RE_THOUGHT_TAGS.sub("", veri.get("thinking", "")).strip()
            except Exception:
                if json_modu:
                    yanit = self.client.generate(model=model_adi, prompt=prompt, format="json", options=opts)
                else:
                    yanit = self.client.generate(model=model_adi, prompt=prompt, options=opts)
                ham = yanit.get("response", "") if isinstance(yanit, dict) else getattr(yanit, "response", "")
        return _RE_THOUGHT_TAGS.sub("", ham).strip()

    @staticmethod
    def _guvenli_json_coz(metin: str) -> dict:
        """Model yanıtı içinde Markdown veya ek açıklama olsa bile JSON nesnesini güvenle ayıklar."""
        if not metin:
            return {}
        temiz = metin.strip()
        try:
            return json.loads(temiz)
        except Exception:
            eslesme = _RE_JSON_OBJ.search(temiz)
            if eslesme:
                try:
                    return json.loads(eslesme.group(0))
                except Exception:
                    pass
        return {}

    # =========================================================================
    # ÖZELLİK 1: RE-RANKING & BİLGİ SIKIŞTIRMA (PROMPT COMPRESSION)
    # =========================================================================
    def ram_ici_rerank_yap(self, model_adi: str, soru: str, baglam_listesi: list) -> str:
        """
        Gelen RAG verilerini RAM üzerinde değerlendirir, puanlar, gereksizleri eler
        ve ardından dolgu kelimelerinden arındırarak "Saf Bilgi Konsantresine" dönüştürür.
        """
        temiz_liste = [m.strip() for m in baglam_listesi if m and len(m.strip()) > 15]
        if not temiz_liste:
            return ""

        filtrelenmis_baglam = []
        for metin in temiz_liste[:4]:
            if not self._devam_edebilir_mi():
                break
            istek = (
                f"Soru: '{soru[:300]}'\n"
                f"Aşağıdaki metin bu soruyu cevaplamak için faydalı mı?\nMetin: {metin[:600]}\n"
                "SADECE JSON FORMATINDA YANIT VER. Örnek: {\"ilgili_mi\": true, \"puan\": 90}"
            )
            try:
                yanit_metin = self._generate_guvenli(
                    model_adi=model_adi,
                    prompt=istek,
                    options={"temperature": 0.0, "num_predict": 60, "num_ctx": self.sabit_ctx},
                    json_modu=True
                )
                sonuc_json = self._guvenli_json_coz(yanit_metin)
                puan = int(sonuc_json.get("puan", 0))
                if sonuc_json.get("ilgili_mi", False) and puan >= 70:
                    filtrelenmis_baglam.append((puan, metin))
            except Exception:
                filtrelenmis_baglam.append((50, metin))

        filtrelenmis_baglam.sort(key=lambda x: x[0], reverse=True)
        en_iyi_metinler = [metin for _, metin in filtrelenmis_baglam[:2]]
        birlesik_metin = "\n\n".join(en_iyi_metinler)[:3500]

        if not birlesik_metin.strip():
            return ""

        sikistirma_istemi = (
            f"Aşağıdaki metni bir Baş Mühendise referans olarak vereceğim. Lütfen tüm gereksiz sohbet ve "
            f"dolgu kelimelerini (ve, veya, bence) at. Sadece sayılar, formüller, tespitler ve kodları "
            f"kısa maddeler halinde özetle (Max Bilgi Yoğunluğu):\n\n{birlesik_metin}"
        )

        try:
            sikismis_yanit = self._generate_guvenli(
                model_adi=model_adi,
                prompt=sikistirma_istemi,
                options={"temperature": 0.1, "num_predict": 450, "num_ctx": self.sabit_ctx}
            )
            if sikismis_yanit:
                return "\n\n--- [BİLGİ YOĞUNLUĞU SIKIŞTIRILMIŞ BAĞLAM] ---\n" + sikismis_yanit
        except Exception:
            pass
        return "\n\n--- [RE-RANKING ONAYLI BAĞLAM] ---\n" + birlesik_metin

    # =========================================================================
    # GÜVENLİK BİLEŞENİ: STATİK (ÇALIŞTIRMADAN) SÖZDİZİMİ (AST) DENETLEYİCİSİ
    # =========================================================================
    @staticmethod
    def _statik_ast_hata_kontrolu(metin: str) -> list:
        hatalar = []
        kod_bloklari = _RE_PYTHON_BLOCK.findall(metin)
        for i, kod in enumerate(kod_bloklari, 1):
            try:
                ast.parse(kod)
            except SyntaxError as e:
                hatalar.append(f"Blok #{i} Satır {e.lineno}: {e.msg}")
            except Exception as e:
                hatalar.append(f"Blok #{i} Genel Hata: {str(e)}")
        return hatalar

    # =========================================================================
    # 6 KATMANLI OTONOM AJAN ZİNCİRİ (ULTIMATE WORKFLOW)
    # =========================================================================
    def ajan_zincirini_baslat(self, model_adi: str, kullanici_sorusu: str, temiz_baglam: str, profil_kurallari: str,
                              ui_guncelleme_fonksiyonu) -> str:

        ui_guncelleme_fonksiyonu("\n[🧠 OTONOM ZEKÂ MERKEZİ AKTİF: 6 Katmanlı Analiz Başlatılıyor...]\n",
                                 tag="telemetry_style")

        # ---------------------------------------------------------
        # AŞAMA 1: DİNAMİK PARAMETRE VE UZUNLUK (ROUTER) MİMARI
        # ---------------------------------------------------------
        ui_guncelleme_fonksiyonu("[1/6] 📐 Mimar Ajan sorunu analiz ediyor ve Adaptif Derinliği belirliyor...\n")
        plan_istemi = (
            f"Soru: {kullanici_sorusu[:1500]}\nBağlam: {temiz_baglam[:1500]}\nKurallar: {profil_kurallari[:1000]}\n\n"
            "Sen bir Baş Mimarsın. Bu sorunun tipini ('kod', 'matematik', 'fikir_tasarimi', 'kisa_cevap') ve "
            "ne kadar uzunlukta bir cevap gerektiğini ('kisa', 'orta', '150_satir_kapsamli') belirle. "
            "Kod ve matematik için sicaklik 0.05, tasarım için 0.4 olmalıdır. "
            "SADECE JSON FORMATINDA YANIT VER. Örnek:\n"
            "{\n  \"sorun_tipi\": \"kod\",\n  \"sicaklik\": 0.05,\n  \"derinlik\": \"150_satir_kapsamli\",\n  \"analiz\": \"Kullanıcı G-Code istemiş...\"\n}"
        )

        dinamik_sicaklik = 0.25
        hedef_derinlik = "orta"
        try:
            plan_yaniti = self._generate_guvenli(
                model_adi=model_adi,
                prompt=plan_istemi,
                options={"temperature": 0.0, "num_predict": 180, "num_ctx": self.sabit_ctx},
                json_modu=True
            )
            mimari_plan = self._guvenli_json_coz(plan_yaniti)
            if mimari_plan:
                dinamik_sicaklik = float(mimari_plan.get("sicaklik", 0.25))
                hedef_derinlik = str(mimari_plan.get("derinlik", "orta"))
                sorun_tipi = str(mimari_plan.get("sorun_tipi", "bilinmiyor")).upper()
                ui_guncelleme_fonksiyonu(
                    f"   ✓ Ayar: Tip={sorun_tipi} | Sıcaklık={dinamik_sicaklik} | Derinlik={hedef_derinlik.upper()}\n")
                plan_metni = json.dumps(mimari_plan, ensure_ascii=False, indent=2)
            else:
                plan_metni = "Soru analiz edildi."
                ui_guncelleme_fonksiyonu("   ⚠ Mimar varsayılan değerlerle devam ediyor.\n")
        except Exception:
            plan_metni = "Soru analiz edildi."
            ui_guncelleme_fonksiyonu("   ⚠ Mimar atlandı, varsayılan değerler devrede.\n")

        if not self._devam_edebilir_mi():
            return "[💤 Otonom işlem kullanıcı tarafından durduruldu.]"

        # ---------------------------------------------------------
        # AŞAMA 2: DÜŞÜNCE AĞACI (MULTI-PATH STRATEGY)
        # ---------------------------------------------------------
        ui_guncelleme_fonksiyonu("[2/6] 🌳 Düşünce Ağacı: Alternatif çözüm yolları üretiliyor...\n")
        tot_istemi = (
            f"Sorun: {kullanici_sorusu[:1500]}\nKurallar: {profil_kurallari[:1000]}\nMimar Planı: {plan_metni}\n\n"
            "Bu sorunu çözmek için 2 FARKLI yaklaşım (A Yolu ve B Yolu) düşün. KOD YAZMA! "
            "Sadece bu iki farklı stratejinin mantığını, avantaj ve dezavantajlarını kıyasla."
        )

        stratejiler = self._generate_guvenli(
            model_adi=model_adi,
            prompt=tot_istemi,
            options={"temperature": 0.3, "num_predict": 550, "num_ctx": self.sabit_ctx}
        )
        ui_guncelleme_fonksiyonu("   ✓ Alternatif stratejiler kıyaslandı.\n")

        if not self._devam_edebilir_mi():
            return "[💤 Otonom işlem kullanıcı tarafından durduruldu.]"

        # ---------------------------------------------------------
        # AŞAMA 3: SENTEZLEYİCİ VE GELİŞTİRİCİ
        # ---------------------------------------------------------
        ui_guncelleme_fonksiyonu("[3/6] 💻 Geliştirici Ajan en iyi stratejiyi koda/rapora dönüştürüyor...\n")
        gelistirici_istemi = (
            f"Kullanıcı Sorusu: {kullanici_sorusu}\nZorunlu Kurallar: {profil_kurallari}\nBağlam: {temiz_baglam[:2000]}\n\n"
            f"Alternatif Stratejiler:\n{stratejiler}\n\n"
            f"Sen bir Sentezleyicisin. Stratejileri incele ve kurallara %100 uyarak NİHAİ YANITI üret. "
            f"Mimarın belirlediği uzunluk hedefi: '{hedef_derinlik}'. Eğer kapsamlı kod isteniyorsa 100-150 satır aralığına ulaş. "
            "Giriş ve çıkışta 'İşte kodunuz', 'Anladım' gibi gereksiz cümleler ASLA kurma."
        )

        nihai_yanit = self._generate_guvenli(
            model_adi=model_adi,
            prompt=gelistirici_istemi,
            options={
                "mirostat": 2,
                "mirostat_tau": 4.5,
                "temperature": dinamik_sicaklik,
                "num_predict": 1800,
                "repeat_penalty": 1.15,
                "num_ctx": self.sabit_ctx
            }
        )
        ui_guncelleme_fonksiyonu("   ✓ İlk sürüm başarıyla üretildi.\n")

        if not self._devam_edebilir_mi():
            return nihai_yanit

        # ---------------------------------------------------------
        # AŞAMA 4: MANTIKSAL VE SEKTÖREL KURAL DENETÇİSİ (SEMANTIC CRITIC)
        # ---------------------------------------------------------
        ui_guncelleme_fonksiyonu(
            "[4/6] ⚖️ Mantıksal Denetçi: Profil kurallarına (G-Code/NASA/Güvenlik) uyum test ediliyor...\n")
        kural_denetim_istemi = (
            f"Zorunlu Kurallar (İhlal Edilmemesi Gerekenler):\n{profil_kurallari[:1200]}\n\n"
            f"Üretilen Yanıt:\n{nihai_yanit[:2500]}\n\n"
            "Sen acımasız bir Sektörel Denetçisin. Üretilen yanıt yukarıdaki kuralların HERHANGİ BİRİNİ (örneğin G00 ile Z- dalışı, "
            "NASA için Halon gazı kullanımı, yarım bırakılmış kod, eksik güvenlik kontrolleri) ihlal ediyor mu? "
            "SADECE JSON YANIT VER. Örnek: {\"kural_ihlali_var\": true, \"ihlal_nedeni\": \"G00 Z- kullanılmış.\", \"duzeltme_talimati\": \"Z ekseni dalışını G01 ile yap.\"}"
        )

        try:
            kural_yaniti = self._generate_guvenli(
                model_adi=model_adi,
                prompt=kural_denetim_istemi,
                options={"temperature": 0.0, "num_predict": 180, "num_ctx": self.sabit_ctx},
                json_modu=True
            )
            kural_json = self._guvenli_json_coz(kural_yaniti)

            if kural_json.get("kural_ihlali_var", False):
                ihlal_nedeni = kural_json.get("ihlal_nedeni", "Bilinmeyen Kural İhlali")
                duzeltme = kural_json.get("duzeltme_talimati", "Kurallara uygun baştan yaz.")
                ui_guncelleme_fonksiyonu(
                    f"   🚨 Mantık/Kural Hatası Tespit Edildi: {ihlal_nedeni}\n   🔄 Otonom olarak yeniden yazdırılıyor...\n",
                    tag="warning_style")

                mantik_duzeltme_istemi = (
                    f"Aşağıdaki metni/kodu yazdın ancak şu kuralı ihlal ettin: {ihlal_nedeni}\n"
                    f"Denetçi Talimatı: {duzeltme}\n\n"
                    f"Lütfen orijinal yapıyı bozmadan sadece bu mantıksal hatayı düzeltip NİHAİ METNİ/KODU tekrar ver:\n\n{nihai_yanit[:2500]}"
                )
                duzeltilmis_mantik = self._generate_guvenli(
                    model_adi=model_adi,
                    prompt=mantik_duzeltme_istemi,
                    options={"temperature": 0.1, "num_predict": 1800, "num_ctx": self.sabit_ctx}
                )
                if duzeltilmis_mantik:
                    nihai_yanit = duzeltilmis_mantik
            else:
                ui_guncelleme_fonksiyonu("   ✓ Üretilen içerik tüm sektörel kurallara (%100) uygun.\n")
        except Exception:
            ui_guncelleme_fonksiyonu("   ⚠ Mantıksal denetim atlandı.\n")

        # ---------------------------------------------------------
        # AŞAMA 5: OTONOM SÖZDİZİMİ DÜZELTİCİ (AST AUTO-FIXER)
        # ---------------------------------------------------------
        ui_guncelleme_fonksiyonu("[5/6] 🛠️ AST Denetleyicisi: Python kod bloklarında sözdizimi kontrol ediliyor...\n")
        deneme = 0
        while deneme < 2 and self._devam_edebilir_mi():
            hatalar = self._statik_ast_hata_kontrolu(nihai_yanit)
            if not hatalar:
                ui_guncelleme_fonksiyonu("   ✓ AST Sözdizimi denetiminden hatasız geçti.\n")
                break

            ui_guncelleme_fonksiyonu(
                f"   ⚠ Sözdizimi Hatası Bulundu! Otonom düzeltme uygulanıyor (Deneme {deneme + 1})...\n",
                tag="warning_style")
            duzeltme_istemi = (
                f"Yazdığın kodda şu Python derleme hataları (SyntaxError) tespit edildi:\n{hatalar}\n\n"
                f"Lütfen orijinal kodundaki sadece bu hatalı kısımları düzelt ve kodu tekrar eksiksiz paylaş. Hatalı Kod:\n{nihai_yanit[:2500]}"
            )
            duzeltilmis_yanit = self._generate_guvenli(
                model_adi=model_adi,
                prompt=duzeltme_istemi,
                options={"temperature": 0.05, "num_predict": 1800, "num_ctx": self.sabit_ctx}
            )
            if duzeltilmis_yanit:
                nihai_yanit = duzeltilmis_yanit
            deneme += 1

        # ---------------------------------------------------------
        # AŞAMA 6: DOĞRULUK VE HALÜSİNASYON DEDEKTÖRÜ (FACT-CHECKER)
        # ---------------------------------------------------------
        if temiz_baglam and "BİLGİ YOĞUNLUĞU" in temiz_baglam and self._devam_edebilir_mi():
            ui_guncelleme_fonksiyonu(
                "[6/6] 🕵️ Halüsinasyon Dedektörü: Veriler orijinal RAG kaynağıyla kıyaslanıyor...\n")
            dedektor_istemi = (
                f"Orijinal Referans Bağlam:\n{temiz_baglam[:1500]}\n\n"
                f"Üretilen Nihai Yanıt:\n{nihai_yanit[:1000]}\n\n"
                "Soru: Üretilen yanıt, orijinal bağlamda HİÇ OLMAYAN uydurma (halüsinasyon) sayılar veya API'ler içeriyor mu? "
                "SADECE JSON FORMATINDA YANIT VER. Örnek: {\"uydurma_var\": false, \"tespit\": \"Uygun\"}"
            )
            try:
                dedektor_yaniti = self._generate_guvenli(
                    model_adi=model_adi,
                    prompt=dedektor_istemi,
                    options={"temperature": 0.0, "num_predict": 120, "num_ctx": self.sabit_ctx},
                    json_modu=True
                )
                dedektor_json = self._guvenli_json_coz(dedektor_yaniti)
                if dedektor_json.get("uydurma_var", False):
                    ui_guncelleme_fonksiyonu(
                        "   ⚠ DİKKAT: Dedektör yanıtta kaynağı belirsiz uydurma veriler saptadı.\n",
                        tag="warning_style")
                    nihai_yanit += "\n\n> 🛡️ **ALTAR GÜVENLİK NOTU:** *Doğruluk Dedektörü, bu yanıttaki bazı sayısal veri veya iddiaların orijinal dokümantasyonla tam örtüşmeyebileceğini tespit etmiştir. Kritik verileri teyit ediniz.*"
                else:
                    ui_guncelleme_fonksiyonu("   ✓ Veriler kaynakla eşleşti, halüsinasyon saptanmadı.\n")
            except Exception:
                ui_guncelleme_fonksiyonu("   ⚠ Dedektör pas geçildi.\n")
        else:
            ui_guncelleme_fonksiyonu("[6/6] 🕵️ Dış veri/kaynak olmadığı için Halüsinasyon Dedektörü atlandı.\n")

        gc.collect()
        ui_guncelleme_fonksiyonu("\n✓ Sentezleme tamamlandı. Otonom onaylı NİHAİ SONUÇ aktarılıyor...\n\n",
                                 tag="code_style")
        return nihai_yanit
