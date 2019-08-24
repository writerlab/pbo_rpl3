tanya = True
while tanya:
  print('== MENU MAKANAN ==')
  print('1. RAMEN BEEF')
  print('2. RAMEN CHICKEN KATSU')
  print('3. PAKET HEMAT 1')
  print('4. PAKET HEMAT 2')
  print('5. SELESAI')
  print('')
  pilih = input('PILIH NOMOR [1/2/3/4/5]: ')
  print('-----------------------------')
  
  if int(pilih) == 1:
    print('RAMEN BEEF')
    print('Rp25.000')
    print('===========================')
  elif int(pilih) == 2:
    print('RAMEN CHICKEN KATSU')
    print('Rp24.000')
    print('===========================')
  elif int(pilih) == 3:
    print('PAKET HEMAT 1')
    print('Rp20.000')
    print('===========================')
  elif int(pilih) == 4:
    print('PAKET HEMAT 2')
    print('Rp20.000')
    print('===========================')
  elif int(pilih) == 5:
    print('Selesai.')
    tanya = False
  else:
    print('Tidak ada nomor', pilih)
    tanya = True