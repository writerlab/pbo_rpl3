kkm = 80

print("===TUGAS 1===")
input("Nama :")
input("Kelas :")
nilai = input("Nilai PTS :")
nilai = int(nilai)

if nilai > 80:
     print("Nilai index : ","A")
elif nilai>kkm:
     print("Nilai index :","B")
else :
     print("Nilai index : ","D")          
