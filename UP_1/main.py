from bidang.persegipanjang import PersegiPanjang
p = PersegiPanjang()

p.panjang = int (input("Nilai Panjang= "))
p.lebar = int(input("Nilai Lebar= "))

print("Luas =", p.luas(), "m2")
print("Keliling =", p.keliling(), "m")