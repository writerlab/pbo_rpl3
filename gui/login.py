#!/usr/bin/env python3
import tkinter
from otentikasi import masuk

form = tkinter.Tk()
form.title('LOGIN')
form.geometry("300x200")

# LABEL
label_user = tkinter.Label(form, text="Username").grid(row=0, column=0, sticky='W')
label_pass = tkinter.Label(form, text="Password").grid(row=1, column=0, sticky='W')

# ENTRY/INPUT
entri_user = tkinter.Entry(form)
entri_pass = tkinter.Entry(form, show='*')

# TOMBOL AKSI: login
login = tkinter.Button(form, text="LOGIN", command=lambda:masuk(entri_user, entri_pass))

entri_user.grid(row=0, column=1, sticky='W')
entri_pass.grid(row=1, column=1, sticky='W')
login.grid(row=2, column=0, sticky='W')

if __name__ == '__main__':
  form.mainloop()