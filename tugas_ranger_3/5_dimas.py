import os

def garis(jenismenu):
    for x in range (10):
        print(jenismenu, end = '')
    print('')

while True:
    
    print('== Menu Operasi File ==')
    print('1. Membuat File')
    print('2. Mengisi File')
    print('3. Membaca File')
    print('4. Menghapus File')
    print('5. Menambahkan Isi File')
    print('6. Selesai')

   
    pilih = input('PILIH NOMOR [1/2/3/4/5/6] : ')
    
    if pilih == '1':
        print("== Membuat File ==")
        try:
            garis('_^_^_')
            file = input("Masukkan Nama File Baru: ")
            f = open (file, "w")
            print("File :" , file, "Sudah Dibuat")
            garis('_^_^_')
            f.close()
        except:
            print("Error")
    elif pilih == '2':
        print("== Mengisi File ==")
        try:
            garis('_^_^_')
            file = input("Masukkan Nama File: ")
            with open(file,"w") as fp:
                tulis = input("Isi File = ")
                fp.write(tulis)
                garis('_^_^_')
                fp.close()
        except:
            print("Error")
    
    elif pilih == '3':
        print("== Membaca File ==")
        try:
            garis('_^_^_')
            file = input("Masukkan Nama File: ")
            with open(file,"r") as fp:
                line = fp.readline()
                while line:    
                    print(line.strip())
                    line = fp.readline()
        except:
            print("Error")
    
    elif pilih == '4':
        print("== Menambahkan Isi File ==")
        try:
            garis('_^_^_')
            file = input("Masukkan Nama File: ")
            with open(file,"a") as fp:
                tulis = input("Tambahkan Isi File = ")
                fp.write(tulis)
                fp.write("\n")
                fp.close()
        except:
            print("Error")
        
    elif pilih == '5':
        print("== menghapus File ==")
        try:
            garis('_^_^_')
            file = input("Masukkan Nama File: ")
            os.remove(file)
            print("File "   , file, "Diisi Oleh" )
            f.close()
        except:
            print("Error")

    elif pilih== '6':
        print("Selesai")
        break
    else:
        print("Tidak Ada Pilihan",pilih)