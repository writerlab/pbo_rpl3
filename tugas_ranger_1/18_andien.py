kkm = 80

print("===TUGAS 1===")
input("NAMA :")
input("KELAS:")
nilai = input("nilai PTS :")
nilai = int(nilai)

if nilai > 80:
    print("nilai index :","A")
elif nilai>kkm:
    print("nilai index :","B")
else :
    print("nilai index :","D")