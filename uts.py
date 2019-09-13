def kali(x,y):
  hasil = int(x) * int(y)
  print(hasil)

def bagi(x,y):
  hasil = int(x) / int(y)
  print(hasil)
  
def tambah(x,y):
  hasil = int(x) + int(y)
  print(hasil)
  
def kurang(x,y):
  hasil = int(x) - int(y)
  print(hasil)
  
while True:
  print('1. Perkalian')
  print('2. Pembagian')
  print('3. Penjumlahan')
  print('4. Pengurangan')
  print('5. Selesai')
  
  pilih = input('Pilih Nomor 1/2/3/4/5: ')
  
  if pilih == '1':
    x = input('X: ')
    y = input('Y: ')
    kali(x,y)
  elif pilih == '2':
    x = input('X: ')
    y = input('Y: ')
    bagi(x,y)
  elif pilih == '3':
    x = input('X: ')
    y = input('Y: ')
    tambah(x,y)
  elif pilih == '4':
    x = input('X: ')
    y = input('Y: ')
    kurang(x,y)
  elif pilih == '5':
    print("Selesai")
    break