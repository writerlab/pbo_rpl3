class Orang:
  def __init__(self, wasta):
    self.wasta = wasta

  def jalan(self):
    return self.wasta," jalan 1 langkah kedepan."

# PENGGUNAAN/PEMANGGILAN OBJEK
orang = Orang("zul hilmi") # PEMBUATAN OBJEK BARU
print(orang.wasta) # MENCETAK DATA DARI OBJEK ORANG
print(orang.jalan)
