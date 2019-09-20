# buat class Segitiga
class Segitiga:
  def __init__(self, a, t, s):
    self.alas = a 
    self.tinggi = t 
    self.sisi = s
    
  def luas(self):
    return (self.alas * self.tinggi)/2
  
  def keliling(self):
    return self.alas + self.tinggi + self.sisi
  
# =================================================
# buat objek
segitiga = Segitiga(5, 7, 12)

# hitung luas segitiga
print("Luas:",segitiga.luas())
print("Keliling:",segitiga.keliling())
  