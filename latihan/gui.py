import tkinter
from tkinter import messagebox

form = tkinter.Tk()
form.geometry("200x200")
form.title("KALKULATOR")

def hitung():
  hasil = float(x.get()) * float(y.get())
  messagebox.showinfo("HASIL PERHITUNGAN", hasil)
  
  
x = tkinter.Entry(form)
y = tkinter.Entry(form)
tombol = tkinter.Button(form, text="Hitung", command=hitung)

x.grid(row=0, column=0)
y.grid(row=1, column=0)
tombol.grid(row=3, column=0)

form.mainloop()