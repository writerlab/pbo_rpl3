import os

while True:
    print("===OPRASI FILE===")
    print("1.Buat File")
    print("2.Isi File")
    print("3.Baca File")
    print("4.Hapus File")
    print("5.Selesai")

    pilih = input("Pilih Nomir[1/2/3/4/5]: ")
    
    if pilih =='1':
        print("---Buat File---")
        try:
            file = input("Nama File Baru: ")
            f = open(file,"w")
            print("file",file,"sudah dibuat")
            f.close()
        except:
            print("eror")
    elif pilih =='2':
        print("---Isi File---")
        try:
            file = input("Nama File: ")
            with open(file,"w") as fp:
                data = input("Isi File: ")
                print("file",file,"diisi oleh",data)
                fp.write(data)
                f.close()
        except:
            print("eror")
    elif pilih =='3':
        print("---Baca File---")
        try:
            file = input("Nama File: ")
            with open(file,"r") as fp:
                line = fp.readline()
                while line:
                    print("isi dari file",file,"adalah",line.strip())
                    line = fp.readline()
        except:
            print("eror")
    elif pilih =='4':
        print("---Hapus File---")
        try:
            file = input("Nama File: ")
            os.remove(file)
            print("file",file,"sudah terhapus")
        except:
            print("eror")
    elif pilih =='5':
        print("Selesai")
        break
    else:
        print("tidak ada pilihan untuk nomor",pilih)