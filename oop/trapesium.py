class Trapesium:
  def __init__(self):
    self.ab = 0
    self.bc = 0
    self.cd = 0
    self.da = 0
    self.t = 0
    
  def luas(self):
    return ((self.ab + self.cd) * self.t) / 2
  
  def keliling(self):
    return self.ab + self.bc + self.cd + self.da
  
trapesium = Trapesium()

trapesium.ab = int(input())
trapesium.bc = int(input())
trapesium.cd = int(input())
trapesium.da = int(input())
trapesium.t = int(input())

print(trapesium.luas())
print(trapesium.keliling())

