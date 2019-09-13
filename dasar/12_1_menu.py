import os
def makanan(nama, harga):
  os.system('clear')
  print(nama)
  print("Rp",harga)
  print('---------------------')
  
  
while True:
  print("=== RESTORAN BAPER ===")
  print("1. NASI T.O")
  print("2. NASI KUNING")
  print("3. NASI + GARAM")
  
  pilih = input('PILIH NOMOR (1/2/3): ') 
  
  if int(pilih) == 1:
    makanan("NASI T.O", "5.000")
  elif int(pilih) == 2:
    makanan("NASI KUNING", "6.000") 
    
