""" operator digunakan untuk melakukan operasi pada variabel dan nilai 
python membagi operator ke beberapa kelompok:
    +	->  Addition	        x + y	
    -	->  Subtraction	        x - y	
    *	->  Multiplication	    x * y	
    /	->  Division	        x / y	
    %	->  Modulus	            x % y	
    **	->  Exponentiation	    x ** y	
    //	->  Floor division	    x // y  
"""

nilai1 = 50
nilai2 = 4

#1 addition 
print(nilai1 + nilai2)

#2 subtraction
print(nilai1 - nilai2)

#3 multiplication
print(nilai1 * nilai2)

#4 division (hasil pembagian berkoma)
print(nilai1 / nilai2)     

#5 modulus (sisa hasil bagi)
print(nilai1 % nilai2)

#6 exponen (bilangan berpangkat)
print(nilai1 ** nilai2)

#7 floor division (hasil pembagian akan dibulatkan)
print(nilai1 // nilai2)

""" === assignment operators === 
operator yang digunakan untuk memberikan nilai pada variabel """
a = 2

'''aritmatika'''
#1
a += 3  #sama dengan a = a + 3

#2
a -= 3  #sama dengan a = a - 2

#3
a *= 3  #sama dengan a = a * 3

'''bitwise'''
#4
a %= 3   # sama dengan a = a % 3

#5
a //= 3  # sama dengan a = a // 3

#6
a **= 3  # sama dengan a = a ** 3

#7
a &= 3   # sama dengan a = a & 3

#8
a |= 3   # sama dengan a = a | 3

#9
a ^= 3   # sama dengan a = a ^ 3

#10
a >>= 3   # sama dengan a = a >> 3

#11
a <<= 3   # sama dengan a = a << 3

''' walrus operator (:=)
menyimpan nilai ke variabel sekaligus dipakai langsung dalam satu ekpresi '''

if (panjang := len("fildza")) > 3:
    print(panjang)
#len("fildza") -> 6
#jadi panjang := 6
#6 > 3 itu true

""" comparison operator (operator perbandingan, yang akan mengembalikan True atau false) """
p = 12
r = 7

print(p == r)   #equal
print(p != r)   #not equal
print(p > r)    #greater than
print(p < r)    #less than
print(p >= r)   #greater than or equal to
print(p <= r)   #less than or equal to

""" === chaining comparison operator ===
menggabungkan beberapa operator perbandingan dalam satu baris,
(python bakal ngecek dari kiri ke kanan)"""

x = 7

print(2 < x < 10)
#x lebih besar dari 2 dan x lebih kecil dari 10

""" logical operators (digunakan untuk menggabungkan beberapa kondisi (pernyataan kondisi)) """

#1 and (True jika semua kondisi True)
nilai = 90

if nilai >= 75 and nilai <= 100:
    print('lulus')

#2 or (True kalau salah satu kondisi True)
nilai = 50

if nilai < 75 or nilai > 100:
    print('nilai tidak valid')

#3 not (negasi)
lulus = False

if not lulus:
    print('tidak lulus')


""" === identify operators (is, is not)=== 
membandingkan apakah dua variabel menunjuk ke objek yang sama di memori
    is() True kalau ada dua variabel yang menunjuk ke objek yang sama
    is not() True kalau dia variabel menunjuk ke objek yang berbeda """

a = [1, 2, 3]
c = a

print(a is c)       #True (objek sama)
print(a is not c)   #False
print(a == c)       #True (nilai sama)
#(==) mengecek apakah nilai dua variabel sama

""" === membership operators (in, not in) ===
mengecek apakah suatu nilai (elemen) ada di dalam sebuah objek atau urutan data (sequence)"""

contoh = 'pija suka eskrim'

print("p" in contoh)        #True, karena "p" ada di dalam string
print("j" not in contoh)    #False, karena "j" terdapat di dalam string
print("pija" in contoh)     #True


""" === bitwise operators ===
melakukan operasi pada bilangan biner (0 dan 1) dan mengolah bit nya,
bukan pada angka desimal secara langsung
## jenis bitwise operator di python :
    &   AND ->  1 kalau dua bit sama-sama 1
    |	OR ->   1 jika salah satu bit bernilai 1
    ^	XOR->	1 kalau bit berbeda
    ~	NOT->	membalik bit
    <<	Left Shift ->	geser bit ke kiri
    >>	Right Shift ->	geser bit ke kanan
"""

print(5 & 3)
#representasi biner dari 5 adalah 0101
#representasi biner dari 3 adalah 0011
#kemudian operator & akan membandingkan bit dan menghasilkan nilai (biner) 0001, yang sama dengan 1

print(5 | 3)
# 5 = 0101
# 3 = 0011
# 0101 | 0011 = 0111 (biner) sama dengan = 7 (desimal)


""" === operator precedence ===
menjelaskan urutan operasi mana dulu yang dikerjakan.
urutan prioritasnya adalah sebagai berikut (dimulai dari yang paling prioritas):
    ()	Tanda kurung
    **	Pangkat
    +x -x ~x	plus unary, minus unary, NOT bitwise
    * / // %	kali, bagi, floor division, sisa bagi
    + -	        Tambah, kurang
    << >>	    Geser bit kiri dan kanan
    &	        AND bitwise
    ^	        XOR bitwise
    |           OR bitwise
    == != >     Perbandingan,  
    >= < <= 
    is is not   identitas,
    in not in	keanggotaan    
    not	        NOT logika
    and	        AND logika
    or	        OR 

note: kalau prioritasnya sama atau setara, kerjakan dari kiri ke kanan
"""

print(12 + (5+2))   #dikerjakan dari bagian yang ada di dalam tanda () terlebih dahulu
print(23 - 3 + 6)   #dikerjakan dari bagian kiri ke kanan, karna prioritasnya setara