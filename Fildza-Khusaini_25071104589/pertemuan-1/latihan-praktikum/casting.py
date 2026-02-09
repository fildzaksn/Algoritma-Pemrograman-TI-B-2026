""" 
===== CASTING =====
casting dalam python menggunakan fungsi konstruktor, di antaranya:
    int()
    float()
    str() 
"""

''' int() '''
contoh1 = int(12)       
#12 akan menjadi 12
#membuat bilangan integer dari integer literal (literal: nilai tetap yang ditulis langsung dalam kode program)

contoh2 = int(12.7)     
#12.7 akan dibulatkan menjadi 12
#membuat bilangan integer dari float literal (dengan menghapus semua desimal)

contoh3 = int("23")     
#"12" akan menjadi 12
#membuat bilangan integer dari string literal (dengan syarat string tersebut mewakili bilangan bulat)


''' float() '''
contoh4 = float(9)        
#9 akan menjadi 9.0
# membuat bilangan float dari integer literal

contoh5 = float(9.6)       
#9.8 akan menjadi 9.8
#membuat bilangan float dari float literal

contoh6 = float("10")
#"10" akan menjadi 10
#membuat bilangan float dari string literal (dengan syarat string tersebut mewakili bilangan float atau int)


''' str() '''
contoh7 = str('dewa 19')
# 'dewa 19' akan menjadi 'dewa 19'
#membuat string dari string literal

contoh8 = str(10)
#10 akan menjadi '10'
#membuat string dari integer literal

contoh9 = str(17.9)
#17.9 akan menjadi '17.9
#membuat string dari float literal

'''list(), tuple(), set(), dict()'''
teks = 'dewa 19'        #string
angkaList = [5,6,7,8]   # list
angkaTuple = (9,10,11)  # tuple
dataDict = {"a": 100, "b": 200}  # dict


contoh10 = list(teks)
print(contoh10)
print(type(contoh10))
#string -> list

contoh11 = tuple(teks)
print(contoh11)
print(type(contoh11))
#string -> tuple

contoh12 = set(teks)
print(contoh12)
print(type(contoh12))
#string -> set

contoh13 = tuple(angkaList)
print(contoh13)
print(type(contoh13))
#list -> tuple

contoh14 = set(angkaList)
print(contoh14)
print(type(contoh14))
# list -> set

contoh15 = list(angkaTuple)
print(contoh15)
print(type(contoh15))
#tuple -> list

contoh16 = list(dataDict)
print(contoh16)
print(type(contoh16))
#dict -> list

contoh17 = tuple(dataDict)
print(contoh17)
print(type(contoh17))
#dict -> tuple


