def sezar_sifrele(metin, kaydirma):
    sifreli_metin = ""

    for harf in metin:
        if harf.isalpha():
            buyuk_harf = harf.isupper()
            harf_index = ord(harf.lower()) - ord('a')
            yeni_index = (harf_index + kaydirma) % 26
            yeni_harf = chr(yeni_index + ord('a'))
            if buyuk_harf:
                yeni_harf = yeni_harf.upper()
            sifreli_metin += yeni_harf
        else:
            sifreli_metin += harf

    return sifreli_metin

def sezar_coz(sifreli_metin, kaydirma):
    return sezar_sifrele(sifreli_metin, -kaydirma)

while True:
    print("\n1. Metni Şifrele")
    print("2. Şifreli Metni Çöz")
    print("3. Çıkış")

    secim = input("Lütfen bir seçenek girin (1, 2 veya 3): ")

    if secim == '1':
        metin = input("İşlenecek metni girin: ")
        kaydirma = int(input("Kaydırma miktarını girin: "))
        sifreli_metin = sezar_sifrele(metin, kaydirma)
        print("Şifrelenmiş Metin:", sifreli_metin)
    elif secim == '2':
        sifreli_metin = input("İşlenecek şifreli metni girin: ")
        kaydirma = int(input("Kaydırma miktarını girin: "))
        cozulmus_metin = sezar_coz(sifreli_metin, kaydirma)
        print("Çözülmüş Metin:", cozulmus_metin)
    elif secim == '3':
        print("Programdan çıkılıyor. İyi günler!")
        break
    else:
        print("Geçersiz bir seçenek girdiniz. Lütfen tekrar deneyin.")
