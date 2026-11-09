# 📖 ALTAR PRO - ÇEVRİMDIŞI SİSTEM VE ÖZELLİK KULLANIM KILAVUZU (README)

> **%100 Yerel • Sıfır İnternet Bağımlılığı • Siber Güvenlik, IDE, CNC & NASA Yarışma Laboratuvarı**

Altar; yapay zeka iletişimi, profesyonel Python IDE geliştirme ortamı, 5-katmanlı siber güvenlik kalkanları, tersine mühendislik araçları, endüstriyel CNC katı model simülasyonu ve NASA mikroçekim yarışma laboratuvarını tek çatı altında birleştiren yüksek performanslı, çevrimdışı çalışabilen hibrit bir mühendislik platformudur.

---

## 📑 İÇİNDEKİLER

1. [Genel Mimari & Hızlı Başlangıç](#1-genel-mimari--hızlı-başlangıç)
2. [Yapay Zeka Sohbet & Kodlama Motoru](#2-yapay-zeka-sohbet--kodlama-motoru)
3. [Siber Güvenlik, Ağ IPS & Canlı Ağ Radarı](#3-siber-güvenlik-ağ-ips--canlı-ağ-radarı)
4. [Python IDE, Editör & Canlı Terminal (F5)](#4-python-ide-editör--canlı-terminal-f5)
5. [Dosya Gezgini & Kriptografik Güvenli Kasa](#5-dosya-gezgini--kriptografik-güvenli-kasa)
6. [Kazınan Veri, Analiz & Turbo Modem QoS](#6-kazınan-veri-analiz--turbo-modem-qos)
7. [CNC G-Code 2D & 3D Katı Model Simülatörü (Haas V34)](#7-cnc-g-code-2d--3d-katı-model-simülatörü-haas-v34)
8. [Tersine Mühendislik, Hex Lab & Derin Paket (DPI)](#8-tersine-mühendislik-hex-lab--derin-paket-dpi)
9. [5-Katmanlı Gelişmiş Antivirüs & EDR Kalkanı](#9-5-katmanlı-gelişmiş-antivirüs--edr-kalkanı)
10. [NASA Mikroçekim & Uzay Telemetri Laboratuvarı](#10-nasa-mikroçekim--uzay-telemetri-laboratuvarı)
11. [Altar Belge & Profesyonel Kelime İşlemci (.altar)](#11-altar-belge--profesyonel-kelime-işlemci-altar)
12. [Multimedya Stüdyosu: Ekran Video, Ses & Kamera](#12-multimedya-stüdyosu-ekran-video-ses--kamera)
13. [En Yüksek Performans & Donanım Optimizasyon Rehberi](#13-en-yüksek-performans--donanım-optimizasyon-rehberi)
14. [Klavye Kısayolları ve Hızlı Erişim](#14-klavye-kısayolları-ve-hızlı-erişim)

---

### 1. Genel Mimari & Hızlı Başlangıç
* **Başlatma:** `Local AI.py` dosyasını çalıştırarak uygulamayı başlatın.
* **Açılış Animasyonu:** Karanlıktan zümrüt yeşili doğaya ve şelaleye açılan 60 FPS sinematik Kiosk tam ekran animasyonu çalışır. İstendiğinde herhangi bir tuş veya fare tıklamasıyla anında geçilebilir.
* **Yapay Zeka Aç/Kapat:** Üst menünün solundaki `🔴 Yapay Zeka: Kapalı` butonuna basarak yeşil `🟢 Yapay Zeka: Açık` konumuna getirin.
* **Motor Seçimi:**
  * **Yerel (Ollama):** İnternetsiz, tamamen yerel ekran kartı ve RAM üzerinden gizli çalışır.
  * **Bulut (API):** Google Gemini modelleri üzerinden yüksek akıl yürütme sağlar.
* **Profil Seçimi:** Hedefinize uygun uzmanlık alanını (`Sohbet`, `Yazılım`, `Siber Güvenlik`, `CNC G-Code`, `Ağ`) belirleyin.

---

### 2. Yapay Zeka Sohbet & Kodlama Motoru
* **Yerel Modeller:** `jaahas/qwen3.5-uncensored:9b`, `deepseek-r1`, `llama3`, `mistral`, `llava`.
* **Ajan Komutları:**
  * `/otonom <görev>` : 6-Katmanlı Otonom Planlama Ajanını devreye alır.
  * `SEARCH:::<sorgu>` : Web araması yapar ve yanıtı özetler.
  * `READ:::<url>` : Web sayfasını salt-okunur kazır.
  * `NASA_SEARCH:::<sorgu>` : NASA bilimsel NTRS arşivinde araştırma yapar.
  * `MEMORY_SEARCH:::<kelime>` : Önceki konuşmalarda vektör araması yapar.
  * `REPO_CLONE:::<url>` : GitHub reposunu salt-okunur inceler.
* **Oturum Yönetimi:** Sol alttaki `Oturumlar` butonuyla eski sohbetleri yükleyin, yeniden adlandırın veya silin.
* **Asenkron Mesaj Kuyruğu (FIFO):** Yapay zeka modeli bir yanıt üretirken yeni bir mesaj yazdığınızda arayüz işlemi kesmez; ileti `⏳ Kuyruk: X mesaj beklemede` göstergesiyle sıraya alınır ve model yanıtı tamamladığında sırayla işlenir.
* **Akıllı Otomatik Kaydırma Anahtarı (`📜 Oto Kaydır`):** Sohbet kutusunun hemen üzerindeki toggle switch. Açıkken yeni mesajlar geldikçe sayfayı otomatik alta kaydırır; kapalıyken geçmiş mesajları ve kodları incelerken sayfa konumunuzu sabit tutar.
* **OpenRouter Canlı API Yöneticisi:** `sk-or-v1-...` anahtarlarını arayüzden canlı doğrulama (`/api/v1/auth/key`), hesap bakiyesi sorgulama, GPT-4o, Claude 3.5 Sonnet, DeepSeek ve Llama modellerini tek tıkla aktif etme ve `.env` dosyasıyla otomatik çift yönlü senkronizasyon.

#### Çok Makineli Ollama Çıkarımı (İsteğe Bağlı)
Birden fazla GPU makinesini GbE üzerinden kullanmak için her worker makinesine aynı modeli kurun; ardından Altar istemcisinin `.env` dosyasına worker adreslerini ekleyin:

```env
ALTAR_OLLAMA_HOSTS="http://192.168.1.41:11434,http://192.168.1.42:11434"
ALTAR_OLLAMA_CONNECT_TIMEOUT="10"
ALTAR_OLLAMA_READ_TIMEOUT="180"
```

Altar her üretim isteğini, seçili modeli içeren sağlıklı bir Ollama worker'ına sırayla gönderir. Ağdan yalnızca sohbet bağlamı ve varsa görsel geçer; model ağırlıkları geçmez. `ALTAR_OLLAMA_HOSTS` ayarlanmazsa uygulama eskisi gibi yalnızca `http://localhost:11434` kullanır. CPU'lu Altar istemcisi, yerel Ollama kurmadan GPU worker'larına bağlanabilir.

Her worker'da Ollama'yı yalnızca güvenilen özel LAN IP'sine bağlayın:

```powershell
$env:OLLAMA_HOST="192.168.1.41:11434"
ollama serve
```

Ollama API'si kimlik doğrulaması sağlamaz. Port 11434'ü internete açmayın, varsayılan olarak `0.0.0.0` kullanmayın ve Windows Güvenlik Duvarı giriş kuralını yalnızca güvenilen istemci/worker IP'leriyle sınırlandırın. Bir worker bağlantısı koparsa Altar diğer uyumlu worker'ı dener; yanıt akışı başladıktan sonra bağlantı koparsa çift veya yarım çıktı oluşturmamak için otomatik tekrar yapılmaz.

---

### 3. Siber Güvenlik, Ağ IPS & Canlı Ağ Radarı
* **Ağ IPS Güvenlik Duvarı:** Uygulama açılışında otomatik olarak devreye girer. Şüpheli paketleri ve bağlantı noktalarını gerçek zamanlı denetler.
* **İnteraktif 2D Siber Ağ Radarı (`altar_ag_radari.py`):** Üst bardaki `🌐 Ağ Radarı` butonuna tıklayarak açılır. 360° döner sonar süpürme çizgisi, konsantrik mesafe halkaları ve ağdaki cihazları temsil eden parlayan hedeflerle çalışır.
* **Hibrit RF Spektrumu & Bluetooth/BLE Radarı (`Guvenlik_Duvari_Tuzakli.py`):** İnternet IP paketlerinin yanı sıra 2.4/5GHz Wi-Fi radyo dalgalarını (SSID, BSSID, Kanal, RSSI dBm, Wi-Fi 6E) ve yakındaki Bluetooth aygıtlarını PyCharm konsolunda canlı analiz eder.
* **Cihaz Ayrıntı Paneli (Inspector):** Radarda tespit edilen herhangi bir hedefe tıklandığında IP adresi, MAC adresi, Cihaz Üreticisi (Vendor OUI), gecikme (ping) süresi ve güvenlik durumunu anlık gösterir.
* **Davetsiz Misafir / İhlal Uyarısı (Intruder Alert):** Ağda ilk defa tespit edilen yabancı/şüpheli bir MAC adresi veya cihaz algılandığında anlık kırmızı flaş ve sesli sinyal uyarısı verir.
* **Zararsız & Pasif Tarama:** Sisteme veya yerel ağa zarar vermemesi için Windows'un yerel `arp -a` önbelleğini ve düşük gecikmeli ICMP paketlerini pasif olarak okur.
* **Karantina Kasası:** Şüpheli dosyaları AES-GCM ile `.altar_karantina` dizininde izole eder.

---

### 4. Python IDE, Editör & Canlı Terminal (F5)
* **Sekme:** `🐍 Python IDE & Editör` sekmesine geçin.
* **Geliştirme:** PyCharm açmadan (~2.65 GB RAM tasarrufuyla) Python kodu yazın ve F5 ile canlı terminalde çalıştırın.
* **AST Denetleyicisi:** Kodu çalıştırmadan önce tehlikeli sistem komutlarına (`shell=True`, `rmdir /s`, şüpheli socket) karşı statik denetim yapar.
* **Pip Yöneticisi:** Yüklü paketleri listeleme ve güncelleme olanağı sunar.

---

### 5. Dosya Gezgini & Kriptografik Güvenli Kasa
* **Dizin Tarayıcı:** Tüm yerel sürücülerinizi (C:, D:, E: vb.) hızla tarayın.
* **Kripto Kasa (AES-256):** Hassas dosyaları kendi şifrenizle kilitleyin (`.altar_kasa`).
* **SHA-256 Doğrulama:** Dosya bütünlüğünü tek tıkla doğrulayın.

---

### 6. Kazınan Veri, Analiz & Turbo Modem QoS
* **Web Kazıma:** NASA NTRS ve kamuya açık kaynaklardan tabloları ve JSON verilerini kazır ve SSD'ye kaydeder.
* **Turbo Modem QoS:** Yerel modem bağlantı gecikmesini (Ping), paket kaybını ve bant genişliği kalitesini analiz eder.
* **Port Yöneticisi:** Çalışan servislerin portlarını güvenle listeler.

---

### 7. CNC G-Code 2D & 3D Katı Model Simülatörü (Haas V34)
* **2D İzometrik:** Altar içine gömülü simülatörde kütük boyutlandırma, mengene payı ve ATC Takım Kütüphanesini (T1-T3) yönetin.
* **PyQt5 OpenGL 3D Katı Model (Swansoft):** `🚀 3D Katı Model Aç` butonuyla tam ekran açılır. G00-G03 dairesel enterpolasyon ve mengene çarpışma analizini akıcı sunar.

---

### 8. Tersine Mühendislik, Hex Lab & Derin Paket (DPI)
* **Salt-Okunur Analiz:** .pyc, .exe, .bin veya .dll dosyalarını çalıştırmadan RAM içinde inceleyin.
* **Disassembly & Decompile:** Python Bytecode çözümler ve Opcode dökümü verir.
* **Hex & Entropi:** Shannon Entropi hesaplayıcısı ile packer ve şifreleme tespit eder.
* **DPI Desync:** Yerel ağ paketlerini ve TLS/SNI uyumluluğunu test eder.

---

### 9. 5-Katmanlı Gelişmiş Antivirüs & EDR Kalkanı (Next-Gen Savunma Cephaneliği)
* **5-Katmanlı EDR Çekirdeği:**
  1. Statik SHA-256 Tehdit İmza Taraması ve Bütünlük Doğrulaması.
  2. Shannon Entropi Radarı (Şifreli fidye yazılımı tespiti).
  3. Davranışsal LOLBins & Script Kod Analizörü (Gizli PowerShell/CMD avcısı).
  4. Fidye Tuzağı (Honeypot / Canary Koruması - Dizin şifreleme algılandığında süreci askıya alır).
  5. İndirilenler & Otomatik Karantina Kalkanı (AES-GCM `.altar_karantina`).

* **6 İleri Düzey Güvenlik Aracı (`altar_gelismis_guvenlik.py`):**
  1. 🧠 **AI Sıfır-Gün Tehdit Açıklayıcısı:** Şüpheli dosyaları çalıştırmadan PE başlığı, Shannon entropi, 15+ kritik Windows API'si ve şüpheli kalıplarla analiz eder; 0-100 risk puanı ve Altar AI Türkçe analiz raporu sunar.
  2. 🌲 **Canlı Süreç Ağacı Radarı:** Çalışan süreçlerin üst-alt (parent-child) ilişkisini inceler, gizli parametreli LOLBin süreçlerini tespit eder; askıya alma (Suspend) ve güvenli sonlandırma (Kill) imkanı sağlar.
  3. 🛡️ **Autoruns & Başlangıç Kalkanı:** Kayıt Defteri (`HKCU/HKLM Run`, `RunOnce`) ve Startup klasörlerindeki gizli kalıcılık mekanizmalarını derinlemesine tarar.
  4. 🔌 **USB Aşı & Flaş Bellek Koruyucusu:** Takılan USB bellekleri algılar, kısayol virüslerini (`.lnk`) listeler ve tek tıkla aşı uygulayarak (`autorun.inf` koruma klasörü) bulaşmaları önler.
  5. 🌐 **C2 Sızıntı & Dış Port Avcısı:** Aktif dış bağlantıları bilinen truva atı / C2 portlarıyla (4444, 1337, 31337 vb.) karşılaştırır ve şüpheli soketleri listeler.
  6. 🔒 **Bütünlük Kalkanı (Hosts & FIM):** Windows `hosts` dosyasını ve DNS yönlendirmelerini denetler; saptırmaları tespit eder ve tek tıkla temiz Microsoft hosts şablonuna döndürür.
  7. 📋 **Pano Kripto Koruyucusu (Clipper Sentinel):** Kopyalanan kripto cüzdan ve IBAN adreslerinin arka planda değiştirilmesini engeller.
  8. 🪟 **Webcam & Mic Casus İzleyici:** Kameraya veya mikrofona erişen süreçleri anlık listeler.
  9. 🍪 **Tarayıcı Çerez Kalkanı:** Chrome/Edge çerez ve şifre veritabanlarına yetkisiz erişimleri denetler.
  10. 📜 **SIEM Olay Günlüğü:** Windows Security loglarından kaba kuvvet ve iz silme eylemlerini listeler.
  11. 🧹 **Güvenli Dosya İmha (DoD 5220.22-M):** Seçilen tekil dosyayı 3 geçişli askeri standartta parçalar (Sistem kalkanı korumalı).
  12. 🌐 **Wi-Fi & ARP Zehirleme Dedektörü:** Ortak ağlardaki sahte ağ geçitlerini ve Man-in-the-Middle saldırılarını tespit eder.

---

### 10. NASA Mikroçekim & Uzay Telemetri Laboratuvarı
* **0G/1G Damlacık & d²-Yasası Simülatörü:** Yerçekimsiz ortamda damlacık çapının zamanla küçülmesini ($d^2 = d_0^2 - K \cdot t$) ve küresel soğuk alev fiziğini simüle eder.
* **Akustik Sonifikasyon & Osiloskop:** Telemetri sayısal verilerini işitilebilir ses frekanslarına dönüştürür; gözle kaçan anomalileri ses dalgasıyla yakalar.

---

### 11. Altar Belge & Profesyonel Kelime İşlemci (.altar)
* **Kelime İşlemci:** Zengin metin biçimlendirme, tablolar, şifreli `.altar` kaydı ve PDF dışa aktarma.
* **Hızlı Açılış:** Gereksiz karşılama sekmeleri kaldırılmıştır; doğrudan temiz çalışma belgesiyle tam ekran açılır.

---

### 12. Multimedya Stüdyosu: Ekran Video, Ses & Kamera
* **🎬 Ekran Video:** Bilgisayar ekranını ve mikrofon sesini sıfır gecikmeyle kaydeder.
* **🎙️ Ses Kaydedici:** Profesyonel stüdyo ses kaydı (.wav) ve dalga formu görselleştirmesi.
* **📷 Kamera:** Webcam görüntüsü kaydeder veya anlık fotoğrafı AI Vision analizine aktarır.

---

### 13. En Yüksek Performans & Donanım Optimizasyon Rehberi
1. **GPU Hızlandırma:** NVIDIA CUDA desteğinin aktif olduğundan emin olun. `num_ctx=2048` ile 6-8 GB VRAM kartlarda sıfır bellek taşmasıyla 45+ token/sn üretim sağlanır.
2. **RAM & Pil Tasarrufu:** Sohbet etmediğinizde `🟢 Yapay Zeka: Açık` butonunu kapatın; model bellekten anında silinir.
3. **Profil Kullanımı:** Kodlama yaparken `Profil: Yazılım` seçeneğini belirleyin; gereksiz sohbet cümleleri atlanarak süre %60 kısalır.

---

### 14. Klavye Kısayolları ve Hızlı Erişim
| Kısayol | İşlev |
|---|---|
| **F11** | Tam Ekran Aç / Kapat (Tüm Pencerelerde) |
| **Esc** | Tam Ekrandan Çık / Pencereli Moda Dön |
| **Ctrl + K** | Hızlı Komut Paletini Aç (Spotlight) |
| **F5** | Python IDE Kodunu Canlı Terminalde Çalıştır |
| **Enter** | Sohbet Mesajını Yapay Zekaya Gönder |
| **Shift + Enter** | Mesaj Kutusunda Yeni Satıra Geç |
| **Ctrl + Tab** | Donanım Kilidi: Klavye ve Fare Girişlerini Anında Kilitle / Çöz |

---

### 15. Python Siber Oyun Merkezi (`🎮 Oyun`)
Altar içerisine tamamen yerli Python motorlarıyla geliştirilmiş 4 siber & retro oyun entegre edilmiştir:
1. **Siber Güvenlik & Şifre Çözücü (Hex Breaker):** Bellek dump blokları arasından hedef hex hash'i bulma, port sızma ve güvenlik duvarı frekans bypass mekanizması.
2. **Galaktik Savunma (Nebula Interceptor):** 60 FPS uzay arcade savaşı; parçacık saçılmaları, lazer topları ve dinamik kalkan yönetimi.
3. **Kuantum Siber Yılan:** Neon matrix ızgarası, kuantum tünelleme ve dinamik hızlanan enerji avı.
4. **Altar Nöral AI Pong Düellosu:** Altar'ın refleks algoritmasına karşı falso ve spin dinamiklerine sahip siber tenis düellosu.
* *Tüm oyunlar '⛶ Tam Ekran Oyna' butonuyla görev çubuğunu kaplayan çerçevesiz tam ekranda oynanabilir.*

---

### 16. Müzik & Sinematik Ses Merkezi (`🎵 Müzik`)
* **YouTube & YouTube Music İndirme:** Arama kutusuna YouTube bağlantısı veya şarkı adı yazılarak en yüksek kalitede ses (192 kbps MP3) doğrudan arka planda indirilir.
* **Arka Planda Kesintisiz Çalma:** Başka sekmelere geçilse veya başka uygulamalarda çalışılsa dahi müzik arka planda çalmaya devam eder.
* **60 FPS Sinematik Animasyon Sahnesi:** Müzik çalarken 3 farklı temada (Zümrüt Doğa Şelalesi, Kozmik Mavi Plazma, Cyberpunk Matrix Spektrumu) canlı animasyonlar eşlik eder. '⛶ Tam Ekran Sinematik' modu ile tüm ekran ambient ışık sahnesine dönüştürülebilir.

---

### 17. Altar Sinematik MP4 Oynatıcı
* Açılan tüm MP4 video medyaları, sinematik parçacık & alev introsuyla başlar ve Windows API (`SetForegroundWindow`) entegrasyonuyla doğrudan çerçevesiz tam ekranda ve odaklanmış olarak açılır.
* **Akıllı HUD Kontrolleri:** Boşluk (Space) ile Oynat/Duraklat, Sol/Sağ ok tuşlarıyla 5 saniye sarma, Yukarı/Aşağı ok ile ses kontrolü ve F11/ESC geçişi sunar.

---

### 18. Otomatik Ollama & Model Kurucusu (`altar_ollama_kurucu.py`)
* Kullanıcı tek bir Windows UAC 'Evet' onayı verdikten sonra:
  1. `https://ollama.com/download` üzerinden resmi kurulumu otomatik indirir.
  2. Windows Defender Güvenlik Duvarı'na otomatik izin kuralı ekler.
  3. `ollama serve` servisini localhost:11434 üzerinde başlatır.
  4. Gerekli yapay zeka modellerini (`jaahas/qwen3.5-uncensored:9b` ve `llava:latest`) otomatik çekerek projeyi tek tıkla çalışmaya hazır hale getirir.

