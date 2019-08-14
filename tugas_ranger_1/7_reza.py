kkm = 70

print("____TUGAS____")
input("Nama :")
input("Kelas :")
nilai = input("Nilai PTS :")
nilai = int(nilai)

if nilai > 60:
    print("Nilai Anda :","A,","SELAMAT!!!")
elif nilai>kkm:
    print("Nilai Anda :","B")
else :
    print("Nilai Anda :","D")