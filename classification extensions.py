import os
def classification():
    main_older = input(r"Klasör İsmi Giriniz:\n")
    extensions = [] #uzantılar depolanacak
    folders = [] #dosyalar depolanacak
    def list_dir():
        for folder in os.listdir(main_older):
            if os.path.isdir(os.path.join(main_older,folder)): # dosyanın klasör olup olmadığını kontrol ediyor.
                continue
            if folder.startswith("."): #dosya gizli dosya mi ? "macOS larda sistemsel oluşan dosyalar için" 
                continue
            else:
                folders.append(folder)
               
    list_dir()
#uzantıları alma
    for folder in folders:
        extension = folder.split(".")[-1]
        if extension in extensions:
            continue
        else:
            extensions.append(extension)
    for extension in extensions: #klasörler oluşturuluyor.
        if os.path.isdir(os.path.join(main_older,extension)):
            continue
        else:
            os.mkdir(os.path.join(main_older,extension))
    for folder in folders:
        extension = folder.split(".")[-1]
        os.rename(os.path.join(main_older,folder),os.path.join(main_older,extension,folder))

if __name__ == "__main__":
    classification()
##__name__ == "__main__" modülü eğer "name" değişkeninin değeri "main" ise, yani bu dosya doğrudan çalıştırılan bir dosyaysa,
#"classification()" adlı bir fonksiyonun çağrılmasını sağlar.