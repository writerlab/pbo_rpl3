import os

while True:
    print("=== OPERASI FILE ===")
    print("1. BUAT FILE")
    print("2. ISI FILE")
    print("3. BACA FILE")
    print("4. HAPUS FILE")
    print("5. SELESAI")

    pilih = int(input("Pilih OPERASI FILE [1/2/3/4/5] : "))

    if pilih == 1:
        print("=== BUAT FILE ===")
        try:
            file = input("Nama File Baru : ")
            f = open(file,"w")
            print("File",file,"Berhasil Dibuat.")
            f.close()
        except:
            print("error?")
            os.system('clear')
    elif pilih == 2:
        print("=== ISI FILE ===")
        try:
            file = input("Nama File : ")
            with open(file,"w") as fp:
                data = input("Isi File : ")
                print("Isi file",file, ": ",data)
                fp.write(data)
                f.close()
        except:
            print("error?")
    elif pilih == 3:
        print("=== BACA FILE ===")
        try:
            file = input("Nama File : ")
            with open(file,"r") as fp:
                line = fp.readline()
                while line:
                    print("Isi file",file,"yaitu",line.strip())
                    line = fp.readline()
        except:
            print("error?")
    elif pilih == 4:
        print("=== HAPUS FILE ===")
        try:
            file = input("Nama File : ")
            os.remove(file)
            print("File",file,"Berhasil Dihapus.")
        except:
            print("error?")
    elif pilih == 5:
        print("=== SELESAI ===")
        break