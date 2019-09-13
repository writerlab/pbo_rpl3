def cek_bilangan(z):
  if z > 0:
    print(z,"adalah bilangan positif")
  elif z < 0:
    print(z,"adalah bilangan negatif")
  else:
    print(z,"adalah NOL")

z = input("Masukkan bilangan bulat: ")
cek_bilangan(int(z))
