def perkalian(entry, hasil):
  entry.insert("end", 'x')

def pembagian(entry, hasil):
  entry.insert("end", '/')

def penjumlahan(entry, hasil):
  entry.insert("end", '+')
  
def pengurangan(entry, hasil):
  entry.insert("end", '-')
  

# SAMA DENGAN
def sama_dengan(entry, hasil):
  teks = entry.get()
  for i in range(len(teks)):
    if teks[i] == 'x':
      x = teks[0:i]
      y = teks[i+1:]
      result = int(x) * int(y)
      break
    if teks[i] == '/':
      x = teks[0:i]
      y = teks[i+1:]
      result = float(x) / float(y)
      break
    if teks[i] == '+':
      x = teks[0:i]
      y = teks[i+1:]
      result = int(x) + int(y)
      break
    if teks[i] == '-':
      x = teks[0:i]
      y = teks[i+1:]
      result = int(x) - int(y)
      break
  hasil.insert("end", result)