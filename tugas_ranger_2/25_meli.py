tanya = True
while tanya :
    print ("== MENU MAKANAN ==")
    print ("1. RAMEN BEEF")
    print ("2. RAMEN CHIKEN KATSU")
    print ("3. PAKET HEMAT 1")
    print ("4. PAKET HEMAT 2")
    print ("5. SELESAI")

    menu = int(input ("PILIH NOMOR 1/2/3/4/5"))
if menu == 1 :
        print ("-------HARGA-------")
        print ("RAMEN BEEF") 
        print ("Rp 25.000")
        print ("===================")
        tanya = True
elif menu == 2 :
        print ("-------HARGA-------")
        print ("RAMEN CHIKEN KATSU")
        print ("Rp 24.000")
        print ("===================")
        tanya = True
elif menu == 3 :
        print ("-------HARGA-------")
        print ("PAKET HEMAT 1")
        print ("Rp 20.000")
        print ("===================")
        tanya = True
elif menu == 4 :
        print ("-------HARGA-------")
        print ("PAKET HEMAT 2")
        print ("Rp 20.000")
        print ("===================")
        tanya = True
elif menu == 5 :
        print ("===================")
        print ("Selesai")
        print ("===================")
        tanya = False
