class Otentikasi:
  def __init__(self):
    self.email = "zul@hilmi.id"
    self.password = "123"
    
  def login(self, input_email, input_password):
    if input_email == self.email:
      if input_password == self.password:
        print("Login Berhasil")