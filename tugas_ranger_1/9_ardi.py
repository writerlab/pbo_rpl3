kkm = 80

print("TUGAS")
input("Nama :")
input("Kelas :")
nilai = input("Nilai PTS :")
nilai = int(nilai)

if nilai > 80:
    print("Nilai Anda :","A,","MANTAP!!!")
if nilai < 79:
    print("Nilai Anda :","C,","Tingkatkan!!!")
elif nilai>kkm:
    print("Nilai Anda :","B")
else :
    print("Nilai Anda :","D")