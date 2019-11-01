import os

def loopsimbol(jenismenu):
    for x in range (20):
        print(jenismenu, end = '')
    print('')

while True:
    
    print('--___--operasi file__--__')
    print('1. buat file')
    print('2. isi file')
    print('3. baca file')
    print('4. hapus file')
    print('5. tambahkan isi file')
    print('6. selesai')


   
    pilih = input('PILIH NOMOR [1/2/3/4/5/6] : ')
    
    if pilih == '1':
        print("=====buatfile========")
        try:
            loopsimbol('-')
            file = input("masukkan nama file baru: ")
            f = open (file, "w")
            print("file :" , file, "sudah dibuat")
            loopsimbol('=')
            f.close()
        except:
            print("error")
    elif pilih == '2':
        print("=====isi file========")
        try:
            loopsimbol('-')
            file = input("masukkan nama file: ")
            with open(file,"w") as fp:
                tulis = input("isi file = ")
                fp.write(tulis)
                loopsimbol('=')
                fp.close()
        except:
            print("error")
    
    elif pilih == '3':
        print("=====baca file========")
        try:
            loopsimbol('-')
            file = input("masukkan nama file: ")
            with open(file,"r") as fp:
                line = fp.readline()
                while line:    
                    print(line.strip())
                    line = fp.readline()
        except:
            print("error")
    
    elif pilih == '4':
        print("=====hapus file========")
        try:
            loopsimbol('-')
            file = input("masukkan nama file: ")
            os.remove(file)
            print("file "   , file, "diisi oleh" )
            f.close()
        except:
            print("error")

    elif pilih == '5':
        print("=====tambahkan isi file========")
        try:
            loopsimbol('-')
            file = input("masukkan nama file: ")
            with open(file,"a") as fp:
                tulis = input("tambahkan isi file = ")
                fp.write(tulis)
                fp.write("\n")
                fp.close()
        except:
            print("error")
    elif pilih== '6':
        print("selesai")
        break
    else:
        print("tidak ada pilihan",pilih)