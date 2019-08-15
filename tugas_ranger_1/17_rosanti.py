print("===INPUT===")
nama = input ('nama: ')
kelas = input ('kelas: ')
nilai = int(input('Nilai PTS:'))

print("===OUTPUT===")
print("Nama:" ,nama)
print("kelas:" ,kelas)
print("Nilai Indeks:",)

if nilai > 84:
    print("A")
elif nilai > 79:
    print("B")
elif nilai > 74:
    print("C")
else:
    print("D")