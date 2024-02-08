import os
import time
import smtplib
from email.mime.text import MIMEText

def check_missing_files(directory, extension):
    # Belirtilen dizindeki tüm dosyaları listele ve alfabetik sırayla sırala
    files = sorted(os.listdir(directory))
    
    # Eksik dosyaları saklamak için bir set oluştur
    existing_files = set()
    for file_name in files:
        if file_name.endswith(extension):
            try:
                file_number = int(file_name.split('.')[0])
                existing_files.add(file_number)
            except ValueError:
                pass

    # İlk dosya numarasını bul
    start_number = min(existing_files) if existing_files else 0

    # Eksik dosyaları kontrol et
    missing_files = []
    for expected_number in range(start_number, start_number + len(existing_files)):
        file_name = f"{expected_number}{extension}"
        if file_name not in files:
            missing_files.append(file_name)

    # Eksik dosya varsa mail gönder
    if missing_files:
        send_email(missing_files)
    else:
        print("Eksik dosya tespit edilemedi.")

def send_email(missing_files):
    # Mail gönderilecek bilgiler
    sender_email = "example@mail.com"
    receiver_email = "example@mail.com"
    password = "example"

    # E-posta konu ve içeriği
    subject = "Eksik Dosya Tespit Edildi"
    body = "Eksik dosyalar:\n" + "\n".join(missing_files)

    # E-posta oluşturma
    message = MIMEText(body)
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = receiver_email

    # SMTP sunucusuna bağlanma ve e-posta gönderme
    try:
        with smtplib.SMTP_SSL("smtp.yandex.com.tr", 465) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())

        print("Mail başarıyla gönderildi.")
    except Exception as e:
        print("Mail gönderilirken hata oluştu:", e)

# Kontrol edilecek dizin ve dosya uzantısı
directory = "path/to/your/directory"
extension = ".txt"

while True:
    check_missing_files(directory, extension)
    # 24 saat bekleme
    time.sleep(24 * 60 * 60)  # 24 saat = 24 * 60 dakika * 60 saniye
