import random

angka_rahasia = random.randint(1,10)

tanya = True
while tanya:
  jawaban = input('Tebak angka antara 1 s.d 10: ')
  if int(jawaban) == angka_rahasia:
    print("Selamat Tebakan Anda Benar!")
    tanya = False
  else:
    print("Jawaban kamu salah!")
    tanya = True

