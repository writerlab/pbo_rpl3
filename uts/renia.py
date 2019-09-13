def perkalian(x, y):
  hasil = int(x) * int(y)
  print("HASIL", hasil)
  
def pembagian(x, y):
  hasil = int(x) / int(y)
  print("HASIL", hasil)
  
def penjumlahan(x, y):
  hasil = int(x) + int(y)
  print("HASIL", hasil)
  
def pengurangan(x, y):
  hasil = int(x) - int(y)
  print("HASIL", hasil)
  
while True:
  print('1. PERKALIAN')
  print('2. PENGURANGAN')
  print('3. PENJUMLAHAN')
  print('4. PENGURANGAN')
  print('5. SELESAI')
  
  pilih = input('PILIH NOMER[1/2/3/4/5]: ')
  
  if int(pilih) == 1:
    print('PERKALIAN')
    x = input('x:')
    y = input('y:')
    perkalian(x, y)
  
  elif int(pilih) == 2:
    print('PEMBAGIAN')
    x = input('x:')
    y = input('y:')
    pembagian (x, y)
  
  elif int(pilih) == 3:
    print('PENJUMLAHAN')
    x = input('x:')
    y = input('y:')
    penjumlahan (x, y)
  
  elif int(pilih) == 4:
    print('PENGURANGAN')
    x = input('x:')
    y = input('y:')
    pengurangan (x, y)
  
  elif int(pilih) == 5:
    print('SELESAI')
    break
  
  else:
    print('TIDAK ADA DALAM MENU', pilih)
    
    
  

  
