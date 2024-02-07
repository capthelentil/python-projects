import os
import time

def dosyalari_kontrol_et(dizin, uzanti):
    dosyalar = os.listdir(dizin)
    beklenen_dosyalar = set(f"{i}.{uzanti}" for i in range(1, len(dosyalar)+1))
    mevcut_dosyalar = set(dosyalar)
    eksik_dosyalar = beklenen_dosyalar - mevcut_dosyalar
    if eksik_dosyalar:
        print("Eksik dosya tespit edildi:")
        for eksik_dosya in eksik_dosyalar:
            print(eksik_dosya)
    else:
        print("Eksik dosya tespit edilemedi.")

def ana_fonksiyon():
    dizin = "D:\Testfile"  # Dosya dizini istenilen şekilde değiştirilebilir. #
    uzanti = "txt"  # Dosya uzantısı istenilen şekilde değiştirilebilir. #

    while True:
        dosyalari_kontrol_et(dizin, uzanti)
        time.sleep(2)  # time.sleep saniye bazlı çalışır #

if __name__ == "__main__":
    ana_fonksiyon()