import tkinter.messagebox

user_db = 'zul'
pass_db = '009'

def masuk(entri_user, entri_pass):
  user = entri_user.get()
  password = entri_pass.get()
  
  # LOGIKA PROSES LOGIN
  if user or password:
    if user == user_db:
      if password == pass_db:
        tkinter.messagebox.showinfo("SUKSES", "LOGIN BERHASIL")
      else:
        tkinter.messagebox.showinfo("ERROR", "PASSWORD SALAH")
    else:
      tkinter.messagebox.showinfo("ERROR", "USERNAME SALAH")
  else:
    tkinter.messagebox.showinfo("Hmmmm", "USERNAME/PASSWORD HARUS DIISI")