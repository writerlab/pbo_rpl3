import os

def perkalian(x, y):
  hasil = int(x) * int(y)
  print("Hasil : ",hasil)
  
def pembagian(x, y):
  hasil = float(x) / float(y)
  print("Hasil : ",hasil)
  
def penjumlahan(x, y):
  hasil = int(x) + int(y)
  print("Hasil : ",hasil)
  
def pengurangan(x, y):
  hasil = int(x) - int(y)
  print("Hasil : ",hasil)
  
while True :
  print("1. PERKALIAN")
  print("2. PEMBAGIAN")
  print("3. PENJUMLAHAN")
  print("4. PENGURANGAN")
  print("5. SELESAI")
  
  pilih = input('PILIH OPERASI : ')
  
  if int(pilih)==1:
    os.system('clear')
    print("PERKALIAN")
    x = input('X : ')
    y = input('Y : ')
    perkalian(x, y)
  elif int(pilih)==2:
    os.system('clear')
    print("PEMBAGIAN")
    x = input('X : ')
    y = input('Y : ')
    pembagian(x, y)
  elif int(pilih)==3:
    os.system('clear')
    print("PENJUMLAHAN")
    x = input('X : ')
    y = input('Y : ')
    penjumlahan(x, y)
  elif int(pilih)==4:
    os.system('clear')
    print("PENGURANGAN")
    x = input('X : ')
    y = input('Y : ')
    pengurangan(x, y)
  elif int(pilih)==5:
    os.system('clear')
    print("SELESAI.")
  else :
    print("Tidak Tersedia.",pilih)