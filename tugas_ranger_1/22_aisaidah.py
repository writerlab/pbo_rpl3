kkm = 70

print("====TUGAS 1====")
input("nama :")
input("kelas :")
nilai = input("nilai PTS :")
nilai = int(nilai)

if nilai > 85:
    print("nilai index :  ","A")
elif nilai>kkm:
    print("nilai index : ","B")
else :
    print("nilai index : ","C")
