email_db = "say@zulhilmi.id"
pass_db  = "123"

input_email = input('Email: ')
input_pass = input('Password: ')

if input_email == email_db and input_pass == pass_db:
  print("LOGIN BERHASIL")
else:
  print("KOMBINASI EMAIL/PASSWORD SALAH!")