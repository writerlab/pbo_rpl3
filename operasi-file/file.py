try:
  nama = input('buat file baru: ')
  f = open(nama, "w")
  f.close()
except:
  print("error?")