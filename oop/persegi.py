class persegi:
  def __init__(self,a,b,c,d):
    self.alas = a 
    self.tinggi = b
    self.lebar = c 
    self.sisi = d 
  def luas(self):
    return (self.alas * self.tinggi * self.lebar * self.sisi)/2
  def keliling(self):
    return (self.alas * self.tinggi * self.lebar * self.sisi)
  
print ("OPERASI LUAS DAN KELILING")
a = input ("masukan nilai alas=")
b = input ("masukan nilai tinggi=")
c = input ("masukan nilai lebar=")
d = input ("masukan nilai sisi=")
persegi = persegi(int(a),int(b),int(c),int(d))

print("keliling nya adalah=",persegi.keliling(),"M")
print("luasnya adalah=",persegi.luas(),"M2")

class segitiga:
  def __init__(self,a,b,c,d):
    self.alas = a 
    self.tinggi = b
    self.lebar = c 
    self.sisi = d 
  def luas(self):
    return (self.alas * self.tinggi * self.lebar * self.sisi)/2
  def keliling(self):
    return (self.alas * self.tinggi * self.lebar * self.sisi)
  
print ("OPERASI LUAS DAN KELILING")
a = input ("masukan nilai alas=")
b = input ("masukan nilai tinggi=")
c = input ("masukan nilai lebar=")
d = input ("masukan nilai sisi=")
segitiga = segitiga(int(a),int(b),int(c),int(d))

print("keliling nya adalah=",persegi.keliling(),"M")
print("luasnya adalah=",persegi.luas(),"M2")


