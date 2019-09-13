import os

def perkalian(x, y):
  hasil = x * y
  print("Hasil =",hasil)

def pembagian(x, y):
  hasil = x / y
  print("Hasil =",hasil)

def penjumlahan(x, y):
  hasil = x + y
  print("Hasil =",hasil)

def pengurangan(x, y):
  hasil = x - y
  print("Hasil =",hasil)

while True:
  print('=== KALKULATOR ===')
  print('[1] PERKALIAN')
  print('[2] PEMBAGIAN')
  print('[3] PENJUMLAHAN')
  print('[4] PENGURANGAN')
  print('[5] SELESAI')
  
  pilih = input('PILIH NOMOR [1/2/3/4/5]: ')
  
  # jika pilih 5
  if pilih == '5':
    # maka selesai.
    print('SELESAI.')
    break
  elif pilih == '1':
    # hapus layar dulu
    os.system('clear')
    print("= PERKALIAN =")
    x = input('X = ')
    y = input('Y = ')
    perkalian(int(x), int(y))
  elif pilih == '2':
    # hapus layar dulu
    os.system('clear')
    print("= PEMBAGIAN =")
    x = input('X = ')
    y = input('Y = ')
    pembagian(float(x), float(y))
  elif pilih == '3':
    # hapus layar dulu
    os.system('clear')
    print("= PENJUMLAHAN =")
    x = input('X = ')
    y = input('Y = ')
    penjumlahan(int(x), int(y))
  elif pilih == '4':
    # hapus layar dulu
    os.system('clear')
    print("= PENGURANGAN =")
    x = input('X = ')
    y = input('Y = ')
    pengurangan(int(x), int(y))
  else:
    # hapus layar dulu
    os.system('clear')
    print('TIDAK ADA NOMOR', pilih)
  