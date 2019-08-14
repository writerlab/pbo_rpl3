kkm = 78

print("TUGAS")
input("Nama :")
input("Kelas :")
nilai = input("Nilai PTS :")
nilai = int(nilai)

if nilai > 78:
    print("Nilai Anda :","A,","Bagus!!!")
if nilai < 78:
    print("Nilai Anda :","C,","Belajar Lagi..")
elif nilai>kkm:
    print("Nilai Anda :","B")
else :
    print("Nilai Anda :","D")