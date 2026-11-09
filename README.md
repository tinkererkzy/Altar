# 🌿 ALTAR — Hibrit Çevrimdışı Yapay Zeka, Siber Güvenlik ve Mühendislik İstasyonu

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python: 3.10+](https://img.shields.io/badge/Python-3.10%2B-brightgreen.svg)](https://www.python.org/)
[![UI: CustomTkinter](https://img.shields.io/badge/UI-CustomTkinter%20%26%20PyQt6-blueviolet.svg)](https://github.com/TomSchimansky/CustomTkinter)
[![AI Engine: Ollama, Gemini & OpenRouter](https://img.shields.io/badge/AI%20Engine-Ollama%20%7C%20Gemini%20%7C%20OpenRouter-orange.svg)](https://openrouter.ai/)
[![Security: 5--Layer EDR](https://img.shields.io/badge/Security-5--Layer%20EDR%20%26%20IPS-red.svg)](https://github.com/Faruk042/Altar)

**ALTAR**; yapay zeka iletişimi, profesyonel Python IDE geliştirme ortamı, 5-katmanlı proaktif siber güvenlik kalkanları, tersine mühendislik araçları, endüstriyel CNC takım yolu ve katı model simülasyonu ile NASA mikroçekim uzay telemetri laboratuvarını tek çatı altında birleştiren yüksek performanslı, **%100 çevrimdışı çalışabilen hibrit bir masaüstü mühendislik platformudur**.

Çekirdek yapay zeka olarak çevrimdışı çalışan `jaahas/qwen3.5-uncensored:9b`, `deepseek-r1` ve `llama3` modellerini; bulutta ise `Google Gemini` modellerini hibrit mimariyle destekler.

---

## 📑 Arayüz ve Sistem Mimarisi

---

### 1. Ana Komuta Merkezi, Donanım Takibi ve Canlı Telemetri
Uygulama başlatıldığında tüm alt modülleri, yapay zeka durumunu ve donanım telemetrisini canlı olarak yönetebileceğiniz yarı-saydam siber cam (glassmorphism) temalı modern bir arayüz sunar.

![Ana Komuta Merkezi](assets/readme_gorseller/01_genel_mimari.png)

* **Canlı Donanım Telemetrisi:** Sağ üst köşedeki HUD çubuğundan anlık **CPU %, RAM (MB ve %), VRAM ve Ağ Gecikmesi (Ping ms)** değerlerini milisaniye hassasiyetinde izleyebilirsiniz.
* **Hibrit Motor Seçimi:** Tek tıkla **Yerel (Ollama)** veya **Bulut (API)** motorları arasında geçiş yapabilirsiniz.
* **Dinamik Model ve Profil:** Çevrimdışı çalışırken `qwen3.5:9b`, `deepseek-r1`, `llama3`; bulutta ise `gemini-2.5/3.0` sürümleri seçilebilir. Seçilen uzmanlık profiline (*Sohbet*, *Yazılım / Kodlama*, *Siber Güvenlik*, *CNC G-Code*, *Ağ Operasyon*) göre yapay zekanın sistem talimatı otomatik olarak optimize edilir.
* **Akıllı VRAM Tasarrufu:** `🔴 Yapay Zeka: Kapalı` butonuyla yapay zeka modeli bellekten tamamen tahliye edilerek dizüstü bilgisayarlarda pil tüketimi %70 azaltılır.
* **Donanım Kilit Motoru (`Ctrl + Tab`):** Bilgisayar başından kısa süreli ayrılmalarda klavye ve fare girişlerini anında kilitleyip yetkisiz erişimi önleyen, 0.35s gecikme (debouncing) filtreli donanım güvenlik kalkanı ve sesli bildirimler (`winsound`).
* **2 Sütunlu Kompakt Eylem Izgarası:** 13+ yardımcı araca (Kamera, Ses, Video, Canva, Oyun, Modeller vb.) hızlı erişim sağlayan ferahlatılmış ve optimize edilmiş menü yerleşimi.

---

### 2. Yerel ve Hibrit Yapay Zeka Sohbet Çekirdeği
Vektörel hafıza (ChromaDB RAG), çoklu dosya besleme ve otonom araç çağırma (Tool Calling) özelliklerini barındıran gelişmiş yapay zeka sohbet laboratuvarıdır.

![Yapay Zeka Sohbet Çekirdeği](assets/readme_gorseller/02_sohbet_ai.png)

* 📄 **Belge Besleme (RAG):** `.pdf`, `.docx`, `.txt`, `.py`, `.json`, `.altar` formatındaki belgeleri sürükle-bırak ile yükleyip anlamsal (semantic) sorgulama yapabilirsiniz.
* 📎 **Görsel Analiz (Vision):** Teknik şemalar, ekran görüntüleri veya fotoğraflar yükleyerek yapay zekadan görsel analiz ve kod çıkarımı alabilirsiniz.
* 🎤 **Sesli Komut (STT):** Entegre konuşma tanıma motoruyla mikrofon üzerinden doğrudan sesli komut verebilirsiniz.
* ⚡ **Ajan Komutları:**
  * `/otonom <hedef>` : 6-Katmanlı otonom planlama motorunu devreye alır.
  * `SEARCH:::<sorgu>` : Web üzerinde araştırma yapıp sonuçları özetler.
  * `NASA_SEARCH:::<konu>` : NASA NTRS bilimsel arşivinde araştırma yapar.
  * `MEMORY_SEARCH:::<kelime>` : Geçmiş sohbet oturumlarında vektörel tarama yapar.
* ⏳ **Asenkron Mesaj Kuyruğu (FIFO):** Yapay zeka modeli yanıt üretirken yeni bir mesaj yazdığınızda iletiniz iptal edilmez veya kaybolmaz; `⏳ Kuyruk: X mesaj beklemede` sayacıyla sıraya alınır ve mevcut yanıt tamamlandığı an sıradaki mesaj modele otomatik iletilir.
* 📜 **Akıllı Otomatik Kaydırma Anahtarı (`📜 Oto Kaydır`):** Sohbet alanının hemen üzerinde yer alan açma/kapama switch'i. Açıkken yeni cevaplar üretildikçe sayfayı otomatik en alta kaydırır; kapalıyken geçmiş mesajları ve kod bloklarını incelerken sayfa konumunu sabit tutarak okuma odağınızı korur.
* 🔑 **OpenRouter Entegrasyonu & Canlı API Yöneticisi:** `sk-or-v1-...` anahtarlarını arayüzden tek tıkla canlı sunucu doğrulaması (`/api/v1/auth/key`), bakiye ve model seviyesi testi, programı yeniden başlatmadan GPT-4o, Claude 3.5 Sonnet, DeepSeek ve Llama modellerini aktif etme ve yerel `.env` dosyasıyla otomatik çift yönlü senkronizasyon.

---

### 3. Sekmeler Gezgini ve Çoklu Görev Yönetimi
Sohbet alanının solunda ve sağında yer alan **📑 Sekmeler** butonları, Altar üzerinde açık olan tüm modülleri ve harici pencereleri tek ekranda listeleyen cam navigatör menüsüdür.

![Sekmeler Gezgini](assets/readme_gorseller/03_sekmeler_gezgini.png)

* **Tek Tıkla Geçiş:** Açılan modal arayüzde tüm aktif sekmeler (Video, Canva, IDE, EDR, Ses, Kamera) listelenir; tıklanan özelliğe anında odaklanılır.
* **HUD Göstergesi:** Hangi özelliklerin arka planda çalıştığını yeşil/mavi durum rozetleriyle bildirir.

---

### 4. Galaktik Savunma Siber Oyunu & Dinlenme Merkezi
Uzun çalışma ve geliştirme seanslarında kullanıcıların odaklanmasını ve reflekslerini tazeleyen, Pygame tabanlı arcade uzay savunma simülasyonudur.

![Galaktik Savunma Siber Oyunu](assets/readme_gorseller/04_siber_oyunlar.png)

* 🚀 **Dinamik Fizik & Lazer:** Yön tuşları veya WASD ile uzay aracını kontrol edin, `Space` ile lazer bataryalarını ateşleyin.
* 🛡️ **Kalkan & Dalga Sistemi:** Düşman akınlarına ve asteroid fırtınalarına karşı kalkan gücünüzü koruyun.
* 🎵 **Siber Ses Efektleri:** 8-bit retro arcade synth sesleri ve dinamik skor sayacı.

---

### 5. Sinematik Müzik Çalar & Ses Stüdyosu
Arka planda çalışabilen, lokal ses dosyalarını ve çevrimiçi parçaları görsel ekolayzer eşliğinde çalan dahili müzik merkezidir.

![Sinematik Müzik Çalar](assets/readme_gorseller/05_muzik_sinematik.png)

* 🎶 **Format Desteği:** MP3, WAV, FLAC, OGG ve AAC formatlarını kayıpsız oynatır.
* 📊 **Canlı Spektrum:** Ses frekanslarına göre gerçek zamanlı dalgalanan siber spektrum dalga animasyonu.
* 🔁 **Çalma Listesi:** Parçaları sırayla, karışık veya döngüsel çalabilme; mini kontrol paneliyle arka planda dinleme.

---

### 6. Sinematik Video Oynatıcı & Medya Merkezi
Eğitim videoları, siber güvenlik konferans kayıtları veya teknik sunumları harici oynatıcıya ihtiyaç duymadan Altar içinde izlemenizi sağlar.

![Sinematik Video Oynatıcı](assets/readme_gorseller/06_sinematik_video.png)

* 🎬 **Donanım Hızlandırma:** MP4, MKV, AVI formatlarını sıfır CPU kaybıyla GPU üzerinden akıcı oynatır.
* ⏩ **Gelişmiş Oynatma Kontrolü:** 0.25x'ten 2.0x'e kadar hızlandırma, kare atlama ve ses eşitleme.
* 📷 **Ekran Yakalama:** Videodan tek tıkla yüksek çözünürlüklü ekran görüntüsü alıp yapay zekaya aktarabilme.

---

### 7. Altar Belge & Profesyonel Kelime İşlemci (.altar / PDF)
Analiz çıktılarını, akademik raporları veya teknik şartnameleri düzenlemek için tasarlanmış zengin biçimlendirmeli tam ekran kelime işlemcidir.

![Altar Belge ve Kelime İşlemci](assets/readme_gorseller/07_canva_ve_belge.png)

* 🖋️ **Zengin Metin Biçimlendirme:** Özel fontlar, renkler, hizalama, tablolar, kod blokları ve semboller.
* 🤖 **AI Entegrasyonu:** Sohbet ekranındaki analiz özetlerini tek tıkla belge içine gömme.
* 💾 **Dışa Aktarma:** Belgelerinizi `.altar`, `.docx`, `.txt` formatlarında kaydetme veya tek tıkla **PDF Çıktısı** alma.

---

### 8. Tek Tıkla Ollama & Yapay Zeka Modelleri Kurucusu
Bilgisayarında Ollama veya yerel yapay zeka modeli yüklü olmayan kullanıcılar için tasarlanmış otomatik sinematik kurulum asistanıdır.

![Ollama ve Model Kurucu](assets/readme_gorseller/08_ollama_kurucu.png)

* ⚡ **Otomatik Donanım Analizi:** Sistemdeki NVIDIA, AMD veya Intel GPU belleğini tespit ederek en uygun modeli önerir.
* 📥 **Sessiz İndirme & Servis Başlatma:** Ollama motorunu ve `jaahas/qwen3.5-uncensored:9b` modelini tek tuşla kurup arka plan servisini ayağa kaldırır.

---

### 9. Siber Güvenlik, Ağ IPS & Canlı 2D Siber Ağ Radarı
Sisteme gelen ve giden tüm ağ trafiğini dinleyen, şüpheli port bağlantılarını tespit eden ve yerel ağı 2D siber arayüzle görselleştiren gerçek zamanlı güvenlik modülüdür.

![Siber Güvenlik ve Ağ Radarı](assets/readme_gorseller/09_guvenlik_ve_radar.png)

* 🌐 **İnteraktif 2D Siber Ağ Radarı (`altar_ag_radari.py`):** 360° sürekli dönen sonar süpürme çizgisi, konsantrik mesafe halkaları ve ağdaki cihazları temsil eden parlayan hedeflerle tam teşekküllü modern siber güvenlik radarı.
* 🔍 **Cihaz Ayrıntı Paneli (Device Inspector):** Radarda tespit edilen herhangi bir hedefe tıklandığında IP adresi, MAC adresi, Tahmini Cihaz Üreticisi (Vendor OUI), gecikme (ping) süresi ve güvenlik durumunu anlık görüntüleme.
* 🚨 **Davetsiz Misafir / İhlal Uyarısı (Intruder Alert):** Ağda ilk defa tespit edilen yabancı/şüpheli bir MAC adresi veya cihaz algılandığında anlık kırmızı flaş ve sesli sinyal uyarısı.
* 🛡️ **Pasif & Zararsız Tarama:** Yerel `arp -a` önbelleğini ve düşük gecikmeli ICMP ping paketlerini pasif olarak okur; sisteme, ağa veya diske hiçbir zarar vermez.
* 📡 **Hibrit RF Spektrumu & Bluetooth/BLE Analizörü (`Guvenlik_Duvari_Tuzakli.py`):** Yalnızca giden internet IP paketlerini değil; ortamdaki 2.4 GHz ve 5 GHz RF radyo frekans dalgalarını (SSID, BSSID, kanal, RSSI dBm sinyal kalitesi, 802.11ax Wi-Fi 6E PHY) ve Bluetooth / BLE çevre aygıtlarını canlı olarak dinleyip PyCharm tarzı terminalde analiz eder.
* 🛡️ **IPS Güvenlik Duvarı:** Bilinen şüpheli sunuculara ve botnet adreslerine giden istekleri gerçek zamanlı engeller.
* ⚠️ **Zararlı Port Taraması:** Dinleyen şüpheli portları (ör. 4444, 1337, 8888) tespit ederek kullanıcıyı uyarır.

---

### 10. Tümleşik Python IDE, Editör & Canlı Terminal (F5)
Harici ağır geliştirme ortamlarına ihtiyaç duymadan Python kodu yazabileceğiniz, hata ayıklayabileceğiniz ve F5 ile çalıştırabileceğiniz tümleşik IDE'dir.

![Python IDE ve Canlı Terminal](assets/readme_gorseller/10_python_ide.png)

* 🐍 **Sözdizimi Vurgulama & Şablonlar:** Python anahtar kelimelerini renklendirir; hazır algoritmaları, soket scriptlerini tek tıkla editöre yükler.
* 🛡️ **AST Güvenlik Taraması:** Kodu çalıştırmadan önce tehlikeli sistem komutlarını (`os.system`, `subprocess`, `rmdir /s`) tespit edip uyarır.
* 🖥️ **Canlı Terminal:** Çıktıları ve hataları alt terminal penceresinde eş zamanlı yazdırır.
* 📦 **Pip Paket Yöneticisi:** Yüklü Python paketlerini inceleme ve yeni kütüphane kurma desteği.

---

### 11. Kriptografik Dosya Kasası (PBKDF2 + Fernet - 4 GB) & Dosya Gezgini
Kullanıcı şifreli dizin ve dosya kilitleme sistemi. Büyük boyutlu dosyaları (4 GB'a kadar video, arşiv, veri setleri) bellek taşması olmadan güvenle şifreler.

![Kriptografik Dosya Kasası](assets/readme_gorseller/11_dosya_gezgini_kasa.png)

* 🔐 **Askeri Düzey Şifreleme:** `PBKDF2-HMAC-SHA256` (200.000 iterasyon + 16-bayt kriptografik tuz) ile üretilen 32-bayt anahtar ve `Fernet (AES-128-CBC + HMAC-SHA256)` koruması.
* 🚀 **4 GB Dosya Desteği:** Bellek optimizasyonlu akış motoru sayesinde yüzlerce megabaytlık veya gigabaytlık video dosyalarını saniyeler içinde şifreler (`.altar_lock`).
* 📄 **SHA-256 Kimlik Kartı:** Dosyaların kriptografik bütünlük özetini tek tıkla hesaplar ve görüntüler.

---

### 12. Yörünge & Web Veri Kazıma Köprüsü, Turbo QoS
Açık kaynaklı web sitelerinden (NASA NTRS, akademik arşivler, haber kaynakları) salt-okunur veri çekmek için geliştirilmiş telemetri köprüsüdür.

![Veri Kazıma ve Turbo Modem QoS](assets/readme_gorseller/12_veri_kazima_modem.png)

* 🌐 **Akıllı Veri Ayıklama:** Tabloları, bağlantıları, başlıkları ve paragrafları ayıklar; SSD üzerine JSON veya Markdown olarak kaydeder.
* ⚡ **Turbo Modem QoS:** Yerel ağ bağlantı gecikmesini (Ping), paket kaybını ve hat stabilitesini test eder.

---

### 13. Endüstriyel CNC G-Code 2D & 3D Katı Model Simülatörü
Talaşlı imalat ve makine mühendisliği iş akışları için iki boyutlu takım yolu görselleştiricisi ve 3D katı model simülatörüdür.

![CNC G-Code 2D ve 3D Simülatör](assets/readme_gorseller/13_cnc_simulator.png)

* ⚙️ **G-Code Düzenleyici:** `G00`, `G01`, `G02`, `G03` kodlarını yazın veya yapay zekadan parça programı üretmesini isteyin.
* 📐 **2D Takım Yolu:** Boşta hızlı hareketleri (kesikli kırmızı) ve talaşlı kesim hareketlerini (düz yeşil) koordinat düzleminde çizer.
* 🧊 **3D Katı Model (Haas V34):** PyQt6 / OpenGL motoruyla mengene, kütük ve 3 eksenli freze hareketlerini 3 boyutta simüle eder.

---

### 14. Siber Tersine Mühendislik, Hex Lab & Derin Paket (DPI)
Çalıştırılabilir dosyaları, Python bytecode'larını ve ağ paketlerini RAM seviyesinde analiz eden siber güvenlik laboratuvarıdır.

![Tersine Mühendislik ve Hex Lab](assets/readme_gorseller/14_tersine_muhendislik.png)

* 🔬 **Hex Viewer & Shannon Entropisi:** Dosyaların ikili (binary) yapısını gösterir; entropi grafiğiyle gizlenmiş (packed) veya şifrelenmiş zararlı kodları saptar.
* 🔍 **Bytecode Disassembler:** `.pyc` dosyalarını kaynak kod düzeyinde Opcode komutlarına ayrıştırır.
* 📡 **DPI Desync Analizi:** Paket başlıklarını ve TLS/SNI yapılandırmasını test eder.

---

### 15. Next-Gen Antivirüs, EDR Kalkanı & İleri Düzey Güvenlik Cephaneliği
Sistemi fidye yazılımlarına (Ransomware), sıfır-gün tehditlerine, truva atlarına ve yetkisiz sızmalara karşı koruyan, sıfır-risk (salt-okunur ve defansif) ilkesiyle çalışan 5-kademeli EDR motoru ve 6 gelişmiş güvenlik aracından oluşan entegre siber güvenlik üssüdür.

![5-Katmanlı EDR Kalkanı](assets/readme_gorseller/15_edr_antivirus.png)

#### 🛡️ 5-Kademeli Çekirdek EDR Savunması:
1. **Katman 1 (İmza & Hash):** Statik SHA-256 Tehdit İmza Taraması ve dosya bütünlük doğrulaması.
2. **Katman 2 (Entropi Analizi):** Shannon Entropi Radarı ile şifrelenmiş/paketlenmiş fidye yazılımı ve trojan tespiti.
3. **Katman 3 (Davranışsal LOLBins):** PowerShell, CMD, WScript gibi sistem araçlarının gizli parametrelerle (`-w hidden`, `-enc`) kullanımını yakalayan bellek bekçisi.
4. **Katman 4 (Honeypot / Yem Koruması):** `Altar_Ransomware_Tuzagi` dizinindeki yem dosyaları denetler; fidye yazılımı şifreleme girişiminde bulunduğu an saldırgan süreci tespit eder ve askıya alır (Suspend).
5. **Katman 5 (Otomatik Karantina):** İndirilenler klasörünü ve zararlı dosyaları güvenli AES-GCM şifreli `.altar_karantina` kasasına izole eder.

#### 🚀 6 İleri Düzey Güvenlik ve Antivirüs Aracı (`altar_gelismis_guvenlik.py`):
* 🧠 **AI Destekli Statik Sıfır-Gün Tehdit Açıklayıcısı:** Şüpheli dosyayı çalıştırmadan PE başlığını, Shannon entropisini, 15+ kritik Windows API çağrısını (`VirtualAllocEx`, `WriteProcessMemory`, `CreateRemoteThread`, `SetWindowsHookEx`), gömülü IP/URL adreslerini ve gizli script kalıplarını tarar. 0-100 risk puanı üretir ve Altar'ın yapay zekasına tek tıkla teknik Türkçe tehdit dökümü yorumlatır.
* 🌲 **Canlı Ebeveyn-Çocuk Süreç Ağacı ve LOLBins Radarı:** Çalışan tüm süreçleri hiyerarşik üst-alt ağaç yapısında listeler. Kötüye kullanılan sistem araçlarını (LOLBins) ve şüpheli alt süreçleri görselleştirir. Kritik Windows süreçlerini koruyan beyaz liste güvencesiyle tek tıkla süreci **Askıya Alma (Suspend)**, **Devam Ettirme (Resume)** veya **Güvenle Sonlandırma (Kill)** imkanı tanır.
* 🛡️ **Windows Otomatik Başlatma ve Kayıt Defteri Kalkanı (Autorun Sentinel):** `HKCU/HKLM Run`, `RunOnce` ve Kullanıcı/Sistem Başlangıç klasörlerini derinlemesine tarar. Temp dizininden veya şüpheli betik uzantılarından (`.vbs`, `.js`, `.bat`, `.ps1`) çalışan gizli kalıcılık (persistence) mekanizmalarını listeler.
* 🔌 **Otomatik USB Aşı & Flaş Bellek Kalkanı:** Bilgisayara takılan çıkarılabilir USB sürücüleri anında algılar; gizli sistem dosyalarını ve kısayol virüslerini (`.lnk`) listeler. Tek tıkla USB belleğe aşı uygulayarak (korumalı salt-okunur `autorun.inf` yapısı) zararlıların flaş bellek üzerinden yayılmasını kesin olarak engeller.
* 🌐 **C2 (Komuta Kontrol) ve Dış Ağ Sızıntı Avcısı:** Aktif dış ağ soketlerini (ESTABLISHED) anlık tarayarak bilinen truva atı ve C2 portları (4444, 1337, 31337, 6667, 8888, 5555 vb.) ile eşleştirir. Şüpheli dış IP bağlantılarını ve ilişkili süreci listeler; tek tıkla Windows Güvenlik Duvarı'nda engelleme olanağı sunar.
* 🔒 **Kritik Sistem Dosyası Bütünlük Kalkanı (File Integrity Monitor - FIM):** Windows `hosts` dosyasını (`C:\Windows\System32\drivers\etc\hosts`) ve DNS yapılandırmasını izler. Phishing veya güvenlik sitelerini saptıran zararlı yönlendirmeleri tespit eder; tek tıkla orijinal temiz Microsoft hosts şablonunu geri yükleme desteği sunar.
* 📋 **Kripto & Pano Hırsızı Koruyucusu (Clipper Sentinel):** Kopyalanan Bitcoin (BTC), Ethereum (ETH), Tron (USDT), Solana ve IBAN adreslerini izler; arka plandaki clipper trojanlarının panoyu gizlice manipüle etmesini engeller.
* 🪟 **Gizli Casus & Donanım Gözetleme Avcısı (Webcam & Mic Sentinel):** Windows resmi ConsentStore telemetrisini okuyarak kamerayı veya mikrofonu kullanan ya da en son erişim sağlayan tüm arka plan süreçlerini listeler.
* 🍪 **Tarayıcı Oturum & Çerez Hırsızı Kalkanı (Infostealer Guard):** RedLine ve Lumma gibi zararlıların Chrome ve Edge tarayıcısının SQLite oturum çerezlerini (`Cookies`) ve şifrelerini (`Login Data`) çalma girişimlerini denetler.
* 📜 **Windows Güvenlik Olay Günlüğü Analizörü (Mini-SIEM):** Windows System ve Security kütüklerindeki kritik olayları (Event 4625: Başarısız Oturum Açma, Event 7045: Yeni Servis, Event 1102: Log Temizleme) analiz ederek Türkçe güvenlik zaman tüneli çıkarır.
* 🧹 **Askeri Standartta Güvenli Dosya İmha Motoru (DoD 5220.22-M):** Kullanıcının seçtiği tekil dosyayı 3 geçişli (0x00, 0xFF ve Kriptografik Rastgele Bayt) yöntemle kalıcı olarak yok eder. Sistem ve proje dizinlerini koruyan kesin engelleme kalkanı içerir; kullanıcının dosyalarını yanlışlıkla silme riski sıfırdır.
* 🌐 **Wi-Fi & DNS Sahte Ağ Geçidi Dedektörü (ARP/DNS Spoofing Watcher):** Kafe, otel veya ortak kablosuz ağlarda ARP zehirlemesi (Man-in-the-Middle) ve sahte DNS saptırmalarını denetler.

---

### 16. NASA Mikroçekim & Uzay Telemetri Laboratuvarı
NASA NTRS bilimsel yayınlarını tarayan, yanma (flame in freefall) deney parametrelerini hesaplayan ve uzay telemetrisini simüle eden özel bilimsel modüldür.

![NASA Mikroçekim Laboratuvarı](assets/readme_gorseller/16_nasa_mikrocekim.png)

* 🛰️ **NTRS Bilimsel Korpus:** NASA açık arşivlerindeki mikroçekim yanma deneylerini tarar.
* 🔥 **Alev & Damlacık Yanma Simülasyonu:** Damlacık çapı, sönme limiti ve yanma süresini hesaplar.
* 📊 **Telemetri İkizi:** Yerçekimsiz ortam kabin basıncı, oksijen oranı ve sıcaklık grafiklerini canlı izler.

---

### 17. Multimedya Ekran, Kamera & Ses Kaydedici
Harici üçüncü parti program kurmaya gerek kalmadan eğitim, sunum ve analiz kayıtları almanızı sağlayan entegre stüdyo modülüdür.

![Multimedya Stüdyosu](assets/readme_gorseller/17_multimedya_studyosu.png)

* 🖥️ **Ekran Kaydedici (FFmpeg):** Tam ekran veya seçili pencereyi 60 FPS kalitede videoya kaydeder.
* 📹 **Kamera Kaydedici (OpenCV):** Web kamerasından yüksek çözünürlüklü görüntü ve video yakalar.
* 🎙️ **Ses Kaydedici:** Mikrofon üzerinden temiz WAV/MP3 formatında ses kaydı alır.

---

### 18. 60 FPS Prosedürel Sinematik Animasyonlar & HUD Arayüz
Her özelliğe ve sekmeye özel olarak tasarlanmış, donanımı yormayan prosedürel animasyon motorudur.

![Sinematik Animasyonlar](assets/readme_gorseller/18_sinematik_animasyonlar.png)

* 🌌 **Nöral Ağ Parçacıkları & Siber Izgara:** Sekmelere göre değişen canlı arka planlar.
* 🛡️ **Kilit & Güvenlik:** Kilit simgesi tıklandığında touchpad ve fare kilitlenir; tekrar basıldığında çözülür.

---

### 19. Donanım & Yüksek Performans Optimizasyon Rehberi
Düşük konfigürasyonlu bilgisayarlardan üst düzey iş istasyonlarına kadar Altar'ı maksimum verimle çalıştırma kılavuzudur.

![Performans Rehberi](assets/readme_gorseller/19_performans_rehberi.png)

---

## 🛠️ Kurulum ve Gereksinimler

### 1. Sistem Gereksinimleri
* **İşletim Sistemi:** Windows 10 / 11 (64-bit)
* **Python:** 3.10, 3.11, 3.12 veya 3.13 (64-bit)
* **Bellek (RAM):** En az 8 GB (16 GB önerilir)
* **Ekran Kartı (İsteğe Bağlı):** NVIDIA GPU (CUDA destekli modeller yerel yapay zeka hızlandırması sağlar)

### 2. Depoyu Klonlama
```bash
git clone https://github.com/Faruk042/Altar.git
cd Altar
```

### 3. Gerekli Kütüphanelerin Kurulumu
```bash
pip install -r requirements.txt
```
*(veya temel kütüphaneleri manuel kurmak için):*
```bash
pip install customtkinter darkdetect Pillow PyQt6 pyqtgraph pygame opencv-python scapy yt-dlp ollama psutil cryptography requests beautifulsoup4 sounddevice soundfile matplotlib python-docx ezdxf
```

### 4. Yerel Yapay Zeka Kurulumu (Ollama)
Altar'ı internet olmadan %100 çevrimdışı çalıştırmak için:
1. [ollama.ai](https://ollama.ai) adresinden Ollama'yı kurun.
2. Terminalden önerilen sansürsüz modeli indirin:
   ```bash
   ollama pull jaahas/qwen3.5-uncensored:9b
   ```
*(Alternatif olarak Altar açılışında 'Ollama Kurucu' butonuna basarak tek tıkla otomatik kurdurabilirsiniz).*

### 5. Çok Makineli Ollama Çıkarımı (İsteğe Bağlı)
Birden fazla GPU makinesini GbE üzerinden kullanmak için her worker'a aynı modeli kurun ve Altar istemcisinin `.env` dosyasına worker adreslerini yazın:
```env
ALTAR_OLLAMA_HOSTS="http://192.168.1.41:11434,http://192.168.1.42:11434"
ALTAR_OLLAMA_CONNECT_TIMEOUT="10"
ALTAR_OLLAMA_READ_TIMEOUT="180"
```
Altar, her üretim isteğini modelin bulunduğu sağlıklı bir Ollama worker'ına sırayla gönderir; ağdan yalnızca sohbet bağlamı/görsel gibi istek verisi geçer, model ağırlıkları geçmez. `ALTAR_OLLAMA_HOSTS` ayarlanmadığında davranış değişmez ve yalnızca `http://localhost:11434` kullanılır. CPU'lu bir Altar istemcisi, yerel Ollama kurmadan GPU worker'larına bağlanabilir.

Her GPU worker'ında Ollama'yı yalnızca güvenilen özel LAN IP'sine bağlayın (örnek):
```powershell
$env:OLLAMA_HOST="192.168.1.41:11434"
ollama serve
```
Windows güvenlik duvarında 11434 girişini yalnızca istemci/worker özel ağ IP'leriyle sınırlandırın. Ollama API'si kimlik doğrulaması sağlamaz; `0.0.0.0` ile varsayılan olarak bağlamayın ve 11434'ü internete açmayın. Worker bağlantısı koparsa Altar bir sonraki uyumlu worker'ı dener; tüm worker'lar erişilemezse hata kullanılan endpointlerle birlikte gösterilir. Akış başladıktan sonra bağlantı koparsa yanıt otomatik tekrarlanmaz; çift/yarım çıktı üretmemek için isteği yeniden gönderin.

### 6. Bulut API Yapılandırması (İsteğe Bağlı)
Altar bulut modellerini (Google Gemini veya OpenRouter - GPT-4o, Claude 3.5, DeepSeek) kullanmak isterseniz, anahtarınızı Altar arayüzündeki **`OpenRouter API Anahtarı Tanımla`** penceresinden tek tıkla canlı doğrulayabilir veya proje kök dizinindeki `.env` dosyasına ekleyebilirsiniz:
```env
GEMINI_API_KEY="your_gemini_api_key_here"
OPENROUTER_API_KEY="sk-or-v1-your_openrouter_key_here"
```

### 7. Uygulamayı Başlatma
```bash
python "Local AI.py"
```
Veya oluşturulan **`Altar`** kısayoluna çift tıklayarak tek tıkla başlatabilirsiniz.

### 8. Tek Başına Çalışan EXE (Program) Oluşturma
Projeyi Python ortamına bağımlı olmadan bağımsız bir masaüstü uygulaması (`.exe`) haline getirmek için iki pratik yöntem mevcuttur:

#### Yöntem A: Tek Tıkla Otomatik Derleme (.bat)
Proje kök dizinindeki `Altar_EXE_Olustur.bat` dosyasına çift tıklayın. Script gerekli bağımlılıkları denetler ve `dist/Altar/Altar.exe` programını sıfır hatayla üretir.

#### Yöntem B: Terminal / Komut Satırından Derleme
1. Proje bağımlılıklarını ve PyInstaller paketleyicisini yükleyin:
   ```bash
   pip install -r requirements.txt
   ```
2. Altar'ın optimize edilmiş hazır spec yapılandırmasıyla derlemeyi başlatın:
   ```bash
   pyinstaller --noconfirm --clean Altar.spec
   ```
3. Derleme tamamlandığında bağımsız yürütülebilir programınız **`dist/Altar/Altar.exe`** konumunda hazır olacaktır! İsteğe bağlı olarak bu dosyaya masaüstü kısayolu oluşturabilirsiniz.

---

## 📄 Lisans

Bu proje **Apache License 2.0** kapsamında lisanslanmıştır. Detaylı bilgi için [LICENSE](LICENSE) dosyasını inceleyebilirsiniz.

```text
Copyright 2026 Faruk Emir Bilgin

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0
```

---

## ⚠️ Güvenlik ve Sorumluluk Reddi

* Altar içerisinde yer alan tersine mühendislik, ağ analizi ve port tarama araçları yalnızca **eğitim, yasal savunma, sızma testi (pen-test) ve sistem denetimi** amacıyla geliştirilmiştir.
* İmalat öncesi üretilen CNC G-Code programlarının gerçek tezgaha aktarılmadan önce simülatörde ve yetkili mühendis gözetiminde kontrol edilmesi zorunludur.
* Bu yazılımın yetkisiz, izinsiz veya yasa dışı ağlarda kullanımından doğabilecek her türlü hukuki sorumluluk tamamen kullanıcıya aittir.
