print("=====input=====")
nama = input ('Nama : ')
#print(nama)

kelas = input ('Kelas : ')
#print(kelas)

nilai = int (input ('Nilai PTS :'))

#proses
if nilai >84:
    indeks = "A"
elif nilai >79:
    indeks = "B"
elif nilai >=74:
    indeks = "C"
else :
    indeks = "D"

print("=====output=====")
print("Nama =",nama)
print("Kelas =",kelas)
print("Nilai Indeks =",indeks)