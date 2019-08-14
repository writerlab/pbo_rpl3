kkm = 75

print("+++TUGAS+++")
input("Nama :")
input("Kelas :")
nilai = input("Nilai PTS :")
nilai = int(nilai)

if nilai > 75:
    print("Nilai Kamu :","A")
elif nilai>kkm:
    print("Nilai Kamu :","B")
else :
    print("Nilai Kamu :","D")