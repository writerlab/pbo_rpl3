import random
import tkinter
import tkinter.messagebox

form = tkinter.Tk()
form.title("== TEBAK ANGKA ==")
form.geometry("300x200")

# method untuk cek jawaban
def cek_jawaban():
  if int(jawaban.get()) == angka_rahasia:
    tkinter.messagebox.showinfo("HORE", "JAWABAN KAMU BENAR!")
  elif int(jawaban.get()) > angka_rahasia:
    tkinter.messagebox.showerror("YAAAHHH", "KELEBIHAN!")
  else:
    tkinter.messagebox.showerror("YAAAHHH", "KURANG! :D")

# acak angka baru
angka_rahasia = random.randint(1, 10)
  
    
# informasi/instruksi game
info = "TEBAK ANGKA DARI 1 s.d. 10"
informasi = tkinter.Label(form, text=info)

# input jawaban
jawaban = tkinter.Entry(form)

# tombol cek jawaban dan tombol acak jawaban
tombol = tkinter.Button(form, text="JAWAB", highlightbackground="#525252", command=cek_jawaban)

# tapelkeun kana form
informasi.grid(column=0, row=0)
jawaban.grid(column=0, row=5)
tombol.grid(column=0, row=10)

# jalankan GUI
# form.mainloop()