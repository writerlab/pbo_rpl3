
print ("=====input=====")
p = input ("nama:")
x = input ("kelas:")
nilai=int(input("nilai pts="))

#proses
if nilai>80 :
     index ="a"
elif nilai<= 80 and nilai> 65:
     index ="B"
elif nilai<= 65 and nilai> 60 :
     index ="C"
else:
     index ="D"
              
print ("=====output=====")
print  ("nama:",p)
print  ("kelas:",x)
print("nilai indeks=",index)
  