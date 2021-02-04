try:
  f = open("user.txt", 'r').read().split("\n")
  for i, line in enumerate(f):
    if i == 0:
      user_db = line
    elif i == 1:
      pass_db = line
  f.close()
except:
  print("Berkas tidak ada")    

print("\n===== Login =====")
input_username = input("Username: ")
input_password = input("Password: ")
print("=================")
if input_username == user_db and input_password == pass_db:
    print("Login berhasil!")
else:
  print("Access denied!")
