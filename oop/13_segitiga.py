# buat clas Segitiga
class Segitiga:
  def __init__(self, a, t):
    self.alas = a
    self.tinggi = t
  
  def luas(self):
    return (self.alas * self.tinggi)/2
  
# =====================================
# buat objek 
segitiga = Segitiga(5, 7)

# hitung luas segitiga
print(segitiga.luas())

