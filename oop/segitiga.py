string = ""
baris = 1

n = int(input('banyaknya baris dan kolom: '))

while baris <= n:
  kolom = baris
  
  while kolom > 0:
    string = string + " * "
    kolom = kolom - 1
    
  string = string + "\n"
  baris = baris + 1
print(string)