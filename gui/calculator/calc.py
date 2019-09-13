#!/usr/bin/env python3
from tkinter import *
from numpad import *
from aritmatika import *

form = Tk()
form.title("Calculator")
form.geometry('350x230')

# BERSIHKAN ENTRY
def bersihkan():
  entry.delete(0, END)
  hasil.delete(0, END)


# ENTRY
entry = Entry(form, width=42, font='Prototype')
hasil = Entry(form, width=42, font='Prototype')

# NUMPAD
tbl0 = Button(form, text='0', width=8, command=lambda:tbl_nol(entry))
tbl1 = Button(form, text='1', width=8, command=lambda:tbl_1(entry))
tbl2 = Button(form, text='2', width=8, command=lambda:tbl_2(entry))
tbl3 = Button(form, text='3', width=8, command=lambda:tbl_3(entry))
tbl4 = Button(form, text='4', width=8, command=lambda:tbl_4(entry))
tbl5 = Button(form, text='5', width=8, command=lambda:tbl_5(entry))
tbl6 = Button(form, text='6', width=8, command=lambda:tbl_6(entry))
tbl7 = Button(form, text='7', width=8, command=lambda:tbl_7(entry))
tbl8 = Button(form, text='8', width=8, command=lambda:tbl_8(entry))
tbl9 = Button(form, text='9', width=8, command=lambda:tbl_9(entry))

# OPERATOR
kali = Button(form, text='X', width=2, command=lambda:perkalian(entry, hasil))
bagi = Button(form, text='/', width=2, command=lambda:pembagian(entry, hasil))
tambah = Button(form, text='+', width=2, command=lambda:penjumlahan(entry, hasil))
kurang = Button(form, text='-', width=2, command=lambda:pengurangan(entry, hasil))

equal = Button(form, text='=', width=8, command=lambda:sama_dengan(entry, hasil))
clear = Button(form, text='C', width=8, command=bersihkan)


# PLACEMENT
entry.grid(row=0, column=0, sticky='W', columnspan=30)
hasil.grid(row=1, column=0, sticky='W', columnspan=30)
tbl7.grid(row=2, column=0, sticky='W')
tbl8.grid(row=2, column=1, sticky='W')
tbl9.grid(row=2, column=2, sticky='W')
tbl6.grid(row=3, column=0, sticky='W')
tbl5.grid(row=3, column=1, sticky='W')
tbl4.grid(row=3, column=2, sticky='W')
tbl3.grid(row=4, column=0, sticky='W')
tbl2.grid(row=4, column=1, sticky='W')
tbl1.grid(row=4, column=2, sticky='W')
tbl0.grid(row=5, column=1, sticky='W')
equal.grid(row=5, column=2, sticky='W')
kali.grid(row=2, column=3, sticky='W')
bagi.grid(row=3, column=3, sticky='W')
tambah.grid(row=4, column=3, sticky='W')
kurang.grid(row=5, column=3, sticky='W')
clear.grid(row=5, column=0, sticky='W')

if __name__ == '__main__':
  form.mainloop()