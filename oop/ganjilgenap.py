class GanjilGenap:
  def __init__(self):
    self.bilangan = 0
    
  def cetak(self):
    for bilangan in range(1, int(self.bilangan) + 1):
      if bilangan % 2 == 1:
        print(str(bilangan) + "\tGanjil")
      else:
        print(str(bilangan) + "\tGenap")
        

gg = GanjilGenap()

gg.bilangan = input("Masukkan Bilangan: ")
gg.cetak()

