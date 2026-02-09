"""
tipe data numbers terbagi menjadi tiga jenis utama : 
    integer (int) -> bilangan bulat baik positif atau negatif,
    float (float) -> bilangan desimal,
    dan complex (complex) -> bilangan riil dan bilangan imajiner

"""
#contoh
bil_integer = -10
bil_float = 12.7
bil_float2 = 13e4           #float juga bisa berupa bilangan berpangkat 10 dengan menggunakan huruf "e" untuk menunjukkan pangkat 10
bil_complex = 2 + 3j

print(type(bil_integer))    # <class 'int'>
print(type(bil_float))      # <class 'float'>
print(type(bil_float2))     # <class 'float'>
print(type(bil_complex))    # <class 'complex'>

""" TYPE CONVERTION (mengubah satu tipe ke tipe lainnya menggunakan method int(), float(), dan complex())"""

satu = 7       #int
dua = 2.3      #float
tiga = 1+ 3j   #complex

a = float(satu)
#mengubah (convert) tipe int menjadi float

b = int(dua)
#convert float menjadi int

c = complex(satu)
#convert int menjadi complex

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

""" RANDOM NUMBER (angka acak)"""
# bukan fungsi random(), tetapi modul bawaan bernama random yang dapat menghasilkan angka acak

import random                   #import modul 'random'
print(random.randrange(1, 10))  
#menampilkan angka random 1 - 9
# aturannya: randrange(start:stop)
#start bersifat inklusif, sedangkan stop bersifat eksklusif, jadi 10 ga termasuk 