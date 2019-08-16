kkm = 80

print("===TUGAS 1===")
input("Nama :")
input("Kelas :")
nilai = input("Nilai PTS :")
nilai = int(nilai)

if nilai > 85:
    print("Nilai Index : A")
elif nilai > 79:
    print("Nilai Index : B")
elif nilai > 74:
    print("Nilai index: C")
else :
    print("Nilai Index : D")
