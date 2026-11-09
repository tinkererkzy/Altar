# -*- coding: utf-8 -*-
"""
Altar Güvenli Başlatıcı ve Otomatik Kurulum Köprüsü (main_altar.py)

1. İleride proje EXE yapıldığında ilk açılışta Ollama ve modellerin durumunu denetler.
2. Eğer sistemde Ollama veya modeller eksikse otomatik olarak Windows Yönetici (UAC)
   yetkisi ister ve sinematik animasyonlu kurulum sihirbazını başlatır.
3. Her şey kuruluysa doğrudan ve sıfır gecikmeyle ana Altar uygulamasını başlatır.
"""

import os
import sys
import runpy

if __name__ == "__main__":
    if sys.stdout is None:
        try:
            sys.stdout = open(os.devnull, "w", encoding="utf-8")
        except Exception:
            pass
    if sys.stderr is None:
        try:
            sys.stderr = open(os.devnull, "w", encoding="utf-8")
        except Exception:
            pass

    dizin = os.path.dirname(os.path.abspath(__file__))
    os.chdir(dizin)
    if dizin not in sys.path:
        sys.path.insert(0, dizin)

    try:
        from dotenv import load_dotenv
        load_dotenv(os.path.join(dizin, ".env"), override=False)
    except Exception:
        pass

    # Uzak worker'lar yapılandırıldıysa CPU istemci makinesinde yerel Ollama kurulumu gerekmez.
    uzak_ollama_yapilandirildi = bool(os.getenv("ALTAR_OLLAMA_HOSTS", "").strip())

    # İleride EXE programı olarak dağıtıldığında otomatik ilk kurulum kontrolü
    try:
        from altar_ollama_kurucu import ollama_kurulum_gerekli_mi, otomatik_sinematik_kurulum_baslat
        if not uzak_ollama_yapilandirildi and ollama_kurulum_gerekli_mi():
            otomatik_sinematik_kurulum_baslat()
            # Kurulum tamamlandıktan sonra çık (kurucu zaten ana programı başlatır)
            sys.exit(0)
    except Exception:
        pass

    hedef = os.path.join(dizin, "Local AI.py")
    runpy.run_path(hedef, run_name="__main__")
