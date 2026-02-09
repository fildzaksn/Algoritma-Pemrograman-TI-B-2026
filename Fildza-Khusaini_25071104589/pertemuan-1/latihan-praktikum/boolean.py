""" boolean memiliki dua nilai, yaitu True dan False yang dipakai untuk menyatakan suatu hasil evaluasi ekspresi.
akan tetapi hasil evaluasi hanya dapat bernilai salah satu, True atau False, tidak keduanya """

#1 ==== membandingkan dua nilai ====
print(7 > 9)    #False
print(7 == 9)   #False
print(7 < 9)    #True

#2 === membandingkan dua nilai menggunakan percabangan if else ===
nilai1 = 127
nilai2 = 97

if nilai1 > nilai2 :
    print('nilai pertama lebih besar')
else :
    print('nilai kedua lebih besar')


#3 === most values are True (note: tanpa pembanding) ===
""" fungsi bool() akan mengevaluasi nilai apapun dan mengembalikan True atau False sebagai hasilnya """

print(bool('hai')) 
#hasilnya bakal True karna gaada pembandingnya
#dan setiap string adalah True, kecuali string kosong.

print(bool(127))
#setiap angka adalah True, kecuali angka 0

print(bool(["apple", "pineapple", "pen"]))
#setiap list, tuple, set, dan dictionary adalah True kecuali nilainya kosong 

#4
'''
Satu nilai lain, atau dalam hal ini objek, juga akan dievaluasi sebagai False, 
yaitu ketika objek tersebut dibuat dari sebuah class yang memiliki fungsi __len__() dan 
fungsi tersebut mengembalikan nilai 0 atau False 
'''
class Kotak:
    def __len__(self):
        return 0

box = Kotak()

print(len(box))     # 0
print(bool(box))    # False

#5 === fungsi dapat mengembalikan nilai boolean ===
def cek_umur(umur):
    return umur >= 18

print(cek_umur(20))  # True
print(cek_umur(15))  # False

#6
''' python juga memiliki banyak fungsi bawaan yang mengembalikan nilai Boolean,
 salah satunya adalah fungsi isinstance()'''

x = 10

print(isinstance(x, int))    # True
print(isinstance(x, str))    # False
#Fungsi isinstance() mengembalikan nilai True jika objek termasuk tipe data yang diperiksa, dan False jika tidak