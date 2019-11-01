import os

while True:
	print ("===Operasi File===")
	print ("1.Buat File")
	print ("2.Isi File")
	print ("3.Baca File")
	print ("4.Hapus File")
	print ("5.Selesai")
	
	pilih = input("Pilih Nomor [1/2/3/4/5] :")
	
	if pilih == '1':
		print ("==Buat file==")
		try:
			nama = input ("Nama file = ")
			f = open (nama, "w")
			print("File", nama, "berhasil dibuat")
			f.close()
		except :
			print ("error?")
	elif pilih == '2':
		print ("==Isi file==")
		try:
			nama = input ("Nama file yg akan diisi = ")
			f = open (nama,"a")
			isi = input ("Silahkan isi = ")
			f.write (isi)
			print ("file", nama, "berhasil diisi", isi)
			f.close()
		except :
			print ("error?")
	elif pilih == '3':
		print ("===Baca File===")
		try :
			nama = input ("Nama file yg akan dibaca =")
			f = open (nama , "r")
			print (f.readlines())
			f.close()
		except:
			print("error?")
	elif pilih == '4':
		print ("===Hapus File===")
		try:
			nama = input ("Nama file yg akan dihapus = ")
			os.remove(nama)
			print ("file", nama, "berhasil dihapus")
		except:
			print("error?")
	elif pilih == '5':
		print ("Selesai, terimakasih:)")
		break
	else :
		print ("Tidak ada nomor", pilih)
		print("Silahkan pilih kembali:)")