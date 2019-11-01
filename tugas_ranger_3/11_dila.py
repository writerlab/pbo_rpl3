import os
def loopsimbol(jenismenu): 
    for x in range (20):
        print(jenismenu, end = '') 
    print('')
while True:
    print('___operasi ﬁle___') 
    print('1. buat ﬁle')
    print('2. isi ﬁle') 
    print('3. baca ﬁle') 
    print('4. hapus ﬁle') 
    print('5. tambahkan isi ﬁle') 
    print('6. selesai')
    
    pilih = input('PILIH NOMOR [1/2/3/4/5/6] : ')
    if pilih == '1': 
        print("=====buatﬁle========") 
        try: 
            loopsimbol('-') 
            ﬁle = input("masukkan nama ﬁle baru: ") 
            f = open (ﬁle, "w") 
            print("ﬁle :" , ﬁle, "sudah dibuat") 
            loopsimbol('=') 
            f.close() 
        except: 
            print("error")
    elif pilih == '2': 
        print("=====isi ﬁle========") 
        try: 
            loopsimbol('-') 
            ﬁle = input("masukkan nama ﬁle: ") 
            with open(ﬁle,"w") as fp:
                tulis = input("isi ﬁle = ") 
                fp.write(tulis) 
                loopsimbol('=') 
                fp.close() 
        except: 
            print("error")
    elif pilih == '3': 
        print("=====baca ﬁle========") 
        try: 
            loopsimbol('-') 
            ﬁle = input("masukkan nama ﬁle: ") 
            with open(ﬁle,"r") as fp: 
                line = fp.readline() 
                while line: 
                    print(line.strip()) 
                    line = fp.readline() 
        except: 
                print("error")
    elif pilih == '4':
        print("=====hapus ﬁle========") 
        try:
            loopsimbol('-')
            ﬁle = input("masukkan nama ﬁle: ")
            os.remove(ﬁle)
            print("ﬁle " , ﬁle, "diisi oleh" ) 
            f.close() 
        except:
            print("error")
    elif pilih == '5':
        print("=====tambahkan isi ﬁle========") 
        try: 
            loopsimbol('-') 
            ﬁle = input("masukkan nama ﬁle: ") 
            with open(ﬁle,"a") as fp: 
                tulis = input("tambahkan isi ﬁle = ") 
                fp.write(tulis) 
                fp.write("\n") 
                fp.close() 
        except:
            print("error") 
    elif pilih== '6':
         print("selesai")        
    else:
         print("tidak ada pilihan",pilih)
         break 