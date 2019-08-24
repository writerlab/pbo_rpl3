# simbolgariscepet
def loopsimbol(jenismenu):
    for x in range (20):
        print(jenismenu, end = '')
    print('')

#proces
def main():

    if menu == 1:
        loopsimbol('-')
        print ("RAMEN BEEF ")
        print ('25.000')
        loopsimbol('=')
        print('')
    elif menu == 2:
        loopsimbol('-')
        print ("RAMEN CHICKEN KATSU")
        print ('24.000')
        loopsimbol('=')
        print('')
    elif menu == 3:
        loopsimbol('-')
        print ("PAKET HEMAT 1")
        print ('20.000')
        loopsimbol('=')
        
    elif menu == 4:
        loopsimbol('-')
        print ("PAKET HEMAT 2")
        print ('20.000')
        loopsimbol('=')
        print('')
    
    elif menu == 5:
        loopsimbol('-')
        print ('selesai.')
    
#perulangan/input
while True:
    
    print('======MENU MAKANAN======')
    print('1. RAMEN BEEF')
    print('2. RAMEN CHICKEN KATSU')
    print('3. PAKET HEMAT 1')
    print('4. PAKET HEMAT 2')
    print('5. SELESAI')

   
    menu = int(input('PILIH NOMOR [1/2/3/4/5]'))

    print('')

    main()
    if menu == 5:
        break            




