def decimal_to_binary(sayi):
    binary = ""
    while sayi > 0:
        kalan = sayi % 2
        binary = str(kalan) + binary
        sayi = sayi // 2
    return binary

def decimal_to_octal(sayi):
    octal = ""
    while sayi > 0:
        kalan = sayi % 8
        octal = str(kalan) + octal
        sayi = sayi // 8
    return octal

def decimal_to_hexadecimal(sayi):
    hexadecimal = ""
    while sayi > 0:
        kalan = sayi % 16
        if kalan < 10:
            hexadecimal = str(kalan) + hexadecimal
          
        else:
                
            hexadecimal = chr(kalan + 55) + hexadecimal
        sayi = sayi // 16
    return hexadecimal


def decimal_to_base3(sayi):
    base3 = ""
    
    while sayi > 0:
        kalan = sayi % 3 
        base3 = str(kalan) + base3
        sayi = sayi // 3
    return base3


def decimal_to_base4(sayi):
    base4 = ""
    while sayi > 0:
        kalan = sayi % 4
        base4 = str(kalan) + base4 
        sayi = sayi // 4
    return base4

def decimal_to_base7(sayi):
    base7 = ""
    while sayi > 0:
        kalan = sayi % 7
        base7 = str(kalan) + base7
        sayi = sayi // 7
    return base7      


sayi = int(input("Sayıyı girin: "))

binary = decimal_to_binary(sayi)
octal = decimal_to_octal(sayi)
hexadecimal = decimal_to_hexadecimal(sayi)
base3 = decimal_to_base3(sayi)
base4 = decimal_to_base4(sayi)
base7 = decimal_to_base7(sayi)


print("2'lik Sistemde: ", binary)
print("8lik Sistemde: ", octal)
print("16 lık Sistemde:", hexadecimal)
print("3 lük Sistemde: ",base3)
print("4 lük Sisteminde", base4)
print("7 lik Sistemde:", base7)

