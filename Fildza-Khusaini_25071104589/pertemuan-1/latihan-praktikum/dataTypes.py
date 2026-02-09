"""
Python memiliki tipe data bawaan sebagai berikut dalam beberapa kategori:
 text type    : str
 numbers      : int, float, complex
 sequence     : list, tuple, range
 mapping      : dict
 set          : set, frozen set
 boolean      : bool
 binary types : bytes, bytearray, memoryview
 none type    : oneType
"""

#dalam python, tipe data ditentukan ketika mengisi nilai ke dalam variabel

tipe1 = 'haii'              #str
tipe2 = 1                   #int
tipe3 = 1.2                 #float
tipe4 = 1+2j                #complex (bil. riil dan bil. imajiner)
tipe5 = True                #bool
tipe6 = [1, 2, 3, 4]        #list
tipe7 = [1, 'halo', 2.3]    #list juga
tipe8 = (5, 6, 7)           #tuple (nilai didalamnya tidak bisa diubah)
tipe9 = {'apple', 'pineapple', 'pen'}   #set
tipe10 = {
    'nama' : 'fildza',                  #dict ('key' : 'key value')
    'kelas' : 'TIB', 
    'nim' : 25071104589
}

''' untuk mengetahui tipe data dari nilai dapat menggunakan fungsi type() '''

print(type(tipe1))
print(type(tipe2))
print(type(tipe3))
print(type(tipe4))
print(type(tipe5))
print(type(tipe6))
print(type(tipe7))
print(type(tipe8))
print(type(tipe9))
print(type(tipe10))

# INDEXING (mengambil satu nilai dari kumpulan nilai dengan mengacu indeksnya)
print(tipe6[2])
print(tipe7[1])
print(tipe8[0])
print(tipe9[1])

#kalau mau ngambil nilai key value dari dict dengan mengacu nama key valuenya.
print(tipe8['nama'])

""" jika ingin menentukan tipe data secara spesifik, gunakan fungsi konstruktornya """

tipe1 = str("hai")
tipe2 = int(12)
tipe3 = float(12.7)
tipe4 = complex(2j)
tipe5 = list(("apple", "pineapple", "pen"))
tipe6 = dict(nama = 'pija', akt = 2025)
