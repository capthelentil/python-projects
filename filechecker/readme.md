## File Check Automation

This Python script is a simple automation tool that checks files in a specific directory with a certain extension. It performs the following functions:

- Checks files in the specified directory.
- Verifies if the expected files have the specified extension.
- Notifies the user if any of the expected files are missing.

### Usage

1. **Setting the `directory` variable**: The `directory` variable at the top of the code specifies the directory where the files to be checked are located. It's important to change this to the actual directory you want to monitor.

2. **Setting the `extension` variable**: The `extension` variable specifies the extension of the files to be checked. This should be changed according to the actual extension you want to check.

3. **Running the Script**: The code continuously runs the `main()` function and performs file checks at regular intervals. When you run the script, it will check the files in the specified directory at intervals.

### Example Usage

For example, if you set the `directory` variable to `"C:/Users/User/path/to/file_folder"` and the `extension` variable to `"txt"`, the script will check all `.txt` files in this folder.

### Caution

- Before running the script, ensure that you have correctly set the directory and file extension settings.
- Running the script in an infinite loop may consume unnecessary system resources. Therefore, adjust the waiting time according to the frequency at which files need to be checked.

This simple script can be used to regularly monitor the presence of specific files and identify any missing files.

##############################

Dosya Kontrolü Otomasyonu
Bu Python betiği, belirli bir dizindeki dosyaları belirli bir uzantı ile kontrol eden basit bir otomasyon aracıdır. Aşağıdaki işlevleri gerçekleştirir:

Belirtilen dizindeki dosyaları kontrol eder.
Beklenen dosyaların belirtilen uzantıya sahip olup olmadığını kontrol eder.
Eğer beklenen dosyalardan herhangi biri eksikse, bunları kullanıcıya bildirir.
Kullanım
dosya_dizini değişkenini ayarlama: Kodun en üstünde bulunan directory değişkeni, kontrol edilecek dosyaların bulunduğu dizini belirtir. Bu dizini, kontrol edilmek istenen gerçek dizine değiştirmek önemlidir.

uzanti değişkenini ayarlama: extension değişkeni, kontrol edilecek dosyaların uzantısını belirtir. Bu, kontrol edilmek istenen gerçek uzantıya göre değiştirilmelidir.

Betik başlatma: Kod, main() fonksiyonunu sürekli olarak çalıştırır ve belirli aralıklarla dosya kontrolünü gerçekleştirir. Betiği çalıştırdığınızda, belirli bir süre boyunca belirtilen dizindeki dosyaları kontrol edecektir.

Örnek Kullanım
Örneğin, eğer dosya_dizini değişkenini "C:/Kullanıcılar/Kullanıcı/adres/dosya_klasörü" olarak ve uzanti değişkenini "txt" olarak ayarlarsanız, betik bu klasördeki tüm .txt dosyalarını kontrol edecektir.

Uyarı
Betiği çalıştırmadan önce, kontrol edilecek dizin ve dosya uzantısı ayarlarınızı doğru bir şekilde yapıp yapmadığınızı kontrol edin.
Betiği sonsuz döngü halinde çalıştırdığınızda, gereksiz sistem kaynakları tüketilebilir. Bu nedenle, dosyaların kontrol edilmesi gereken sıklığına uygun olarak bekleme süresini ayarlayın.
Bu basit betik, belirli dosyaların varlığını düzenli olarak izlemek ve eksik dosyaları belirlemek için kullanılabilir.