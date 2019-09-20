import os

def perkalian(x, y):
  hasil= x * y
  print("hasil =",hasil)
  
def pembagian(x, y):
  hasil = x / y
  print("hasil =",hasil)
  
def penjumlahan(x, y):
  hasil = x + y
  print("hasil =",hasil)
  
def pengurangan(x, y):
  hasil = x - y
  print("hasil =",hasil)
  
while True:
  print('====kalkulator====')
  print('[1] perkalian')
  print('[2] pembagian')
  print('[3] penjumlahan')
  print('[4] pengurangan')
  print('[5] selesai')
  
pilih = input ('pilih nomor = [1/2/3/4/5]):

# jika pilih 5
if pilih =='5':
  # maka selesai.
  print('selesai')
  break
elif pilih =='1':
  # hapus layar dulu
  os.system('clear')
  print("= perkalian =")
  x = input('x = ')
  y = input('y = ')
 








