class GanjilGenap:
    def __init__(self):
        self.nomor = 0

    def cek_gan_gen(self):
        for bilangan in range(1,self.nomor):
            try:
                f = open('ganjil.txt','a')
                if bilangan % 2 == 1:
                    f.write(str(bilangan)+"ganjil")
                    f.write('\n')
                    f.close()
                else:
                    f.write(str(bilangan)+"genap")
                    f.write('\n')
                    f.close()
                    

            except:
                print('error')

gg = GanjilGenap()
gg.nomor = int(input("masukkan bilangan :"))
gg.cek_gan_gen() 
            