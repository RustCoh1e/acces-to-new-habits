import os
from datetime import datetime
def classification():
    main_folder = input(r"Klasör İsmi Giriniz:")
    files = [] #dosyalar depolanacak
    dates = [] #tarih bilgileri depolanacak
    def list_dir():
        for file in os.listdir(main_folder):
            if os.path.isdir(os.path.join(main_folder,file)): # dosyanın klasör olup olmadığını kontrol ediyor.
                continue
            if file.startswith("."):
                continue
            else:
                files.append(file)               
    list_dir()
    #Tarihleri Alma
    for file in files:
        birth_time = datetime.fromtimestamp(os.stat(os.path.join(main_folder,file)).st_ctime).strftime("%d-%m-%Y")
        if birth_time in dates:
             continue
        else:
             dates.append(birth_time)
    #klasör oluşturulacak.
    for birth_time in dates:
         if os.path.isdir(os.path.join(main_folder,birth_time)):
              continue
         else:
              os.mkdir(os.path.join(main_folder,birth_time))
    for file in files:
        birth_time = datetime.fromtimestamp(os.stat(os.path.join(main_folder,file)).st_ctime).strftime("%d-%m-%Y")
        os.rename(os.path.join(main_folder,file),os.path.join(main_folder,birth_time,file))

if __name__ == "__main__":
    classification()