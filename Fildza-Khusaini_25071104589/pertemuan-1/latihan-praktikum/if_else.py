""" === python IF ===
Python menggunakan operator perbandingan untuk mengevaluasi kondisi, 
kondisi tersebut biasanya digunakan dalam if statement untuk menentukan apakah kode dijalankan atau tidak
python mendukung kondisi logika seperti di matematika:
    Equals: a == b
    Not Equals: a != b
    Less than: a < b
    Less than or equal to: a <= b
    Greater than: a > b
    Greater than or equal to: a >= b 
"""
#contoh
x = 12
y = 7

#1
if x > y :
    print("nilai x lebih besar daripada y")
#Python menggunakan indentasi untuk menentukan blok atau ruang lingkup kode.

#2 MULTIPLE STATEMENTS in if block
nilai = 90

if nilai >= 80:
    print("cie")
    print("kamu lulus")
    print("pertahankan ya")
#di dalam satu if block, boleh nulis lebih dari satu pernyataan (statement).
#Semua pernyataan tersebut harus memiliki indentasi yang sama.

#3 using variables in conditions   
''' python bisa mengevaluasi banyak tipe data sebagai True atau False di dalam if,
nilai kosong dan nol dianggap False, sedangkan nilai lain dianggap True.'''

is_login = True

if is_login:
    print("kamu udah login")    #True

"""=== elif statement ===
kalau kondisi pertama tidak benar, maka kondisi kedua akan di cek """
a = 11
b = 11

if a > b:
    print('a lebih besar dari b')
elif a == b:
    print('a dan b bernilai sama')
#python akan mengecek kondisi pertama, jika bernilai True maka kondisi pertama dijalankan
#jika False maka akan mengecek kondisi berikutnya, dan berhenti di kondisi pertama yang bernilai True

""" === multiple elif statement ===
menggunakan lebih dari satu elif untuk mengecek banyak kondisi secara berurutan
python tidak menjalankan semuanya, hanya satu, jadi urutan elif itu penting
"""
skor = 75

if skor >= 90:  #False
  print('sangat baik')
elif skor >= 80:    #False
  print('baik')
elif skor >= 70:    #True, perintah akan di cetak dan elif setelahnya ga di cek lagi 
  print('cukup baik')
elif skor >= 60:
  print('belajar lagi ya')

#jadi Gunakan elif saat hanya satu kondisi yang boleh True,
#karena lebih efisien dan lebih tepat secara logika dibandingkan banyak if terpisah

""" === else statement ===
keyword else menangkap semua kondisi yang tidak tertangani oleh kondisi sebelumnya.
pernyataan else dijalankan ketika kondisi if (dan semua elif) bernilai False"""

#contoh complete if-elif-else chain
umur = 20

if umur < 13:   #false
    print("masih anak-anak")
elif umur < 18:     #false
    print("remaja")
else:       
    print("dewasa")
#karna kondisi diatas False semua, jadi else dijalankan

#bisa juga pakai else tanpa elif
a = 23
b = 26
if a > b:
   print('nilai a lebih besar dari b')
else:
   print('nilai b lebih besar dari a')

#else as fallback (cadangan), jadi else cocok sebagai validasi, penanganan error, dan memberi nilai default     
#contoh menangani error
menu = 2

if menu == 1:
   print('login')
else:
   print('pilihan tidak valid')

"""=== short hand if === """
#menulis (hanya) satu perintah dibaris yang sama dengan if

bigger = x if x > y else y    #bigger = x jika x lebih besar dari y, atau bigger = y jika y lebih besar dari x  
print("bigger is", bigger)
#contoh statement if-else di satu baris yang sama untuk memilih sebuah nilai lalu menyimpannya ke dalam variabel


""" === short hand if else===
satu perintah untuk if dan satu perintah untuk else,
ditulis dalam satu baris menggunakan conditional expression (ekspresi kondisi)."""

nilai = 80      
print("Lulus") if nilai >= 75 else print("Tidak lulus")
#cetak 'lulus' jika nilai lebih besar atau sama dengan 75, jika False maka cetak 'tidak lulus'

''' multiple conditions on one line '''
umur = 20

ket = "anak-anak" if umur < 13 else "Remaja" if umur < 18 else "Dewasa"
#True pertama
#cek kedua kalau gagal
#fallback terakhir
print(ket)


""" 
=== and operator ===
keduanya harus benar, jika salah satunya salah maka hasilnya False
"""
nilai = 80
absen = 85

if nilai >= 75 and absen >= 80:   # dua syarat harus terpenuhi
    print("Lulus")
else:
    print("Tidak lulus")
#kedua perbandingan bernilai True, maka hasilnya True dan perintah print akan dijalankan

"""
=== or operator ===
salah satunya harus bernilai True
"""
a = 5
b = 10

if a > 7 or b > 7:  #jika nilai a lebih besar daripada 7, atau nilai b lebih besar daripada 7, maka cetak:
    print("ada yang lebih besar dari 7")
#kondisi a > 7 bernilai True, jadi perintah dijalankan

"""
=== not operator === 
membalik hasil dari sebuah kondisi (negasi)
"""
a = 5

if not a > 10:   #kebalikan dari (a > 10)
    print("a tidak lebih dari 10")
#kondisi a > 10 bernilai False, not False berati True
#jadi print dijalankan

""" combining multiple operators 
python akan mengevaluasi dari urutan prioritas yaitu tanda kurung (), lalu not, lalu and, terakhir or"""
umur = 16
punya_izin = False

if not punya_izin or umur >= 17:
    print("Tidak boleh masuk")
#dievaluasi dari not dulu
#kondisi pertama (punya_izin) bernilai False, jadi not punya_izin = True
#kondisi kedua bernilai False
#True or False = True, karna salah satunya True. jadi aksi dijalankan

""" === nested if statements (if bersarang) ===
menaruh if di dalam if.
jadi kode akan mengecek dari kondisi paling luar dulu, lalu masuk ke dalam
"""
umur = 18
punya_ktp = True

if umur >= 17:                 # cek dulu umur cukup atau tidak
    if punya_ktp:              # kalau umur cukup, baru cek KTP
        print("boleh masuk")   # kalau dua-duanya benar

""" === multiples levels of nesting === """
umur = 20
punya_tiket = True
punya_ktp = True

if umur >= 17:                        # level 1 dicek umur
    if punya_tiket:                   # level 2 cek tiket
        if punya_ktp:                 # level 3 cek KTP
            print("Boleh masuk")      # kalau semua syarat lolos, print dijalankan

""" === nestef if vd logical operators ===
nested if bisa disederhanakan menggunakan operator logika seperti and, tergantung pada logikanya.
kedua cara menghasilkan hasil yang sama.
gunakan nested if kalau logika di dalam lebih kompleks /bertahap,
dan gunakan and kalau kondisinya simpel dan sama penting"""

umur = 18
punya_ktp = True

#contoh bertahap
if umur >= 17:                # cek umur dulu
    if punya_ktp:             # kalau umur cukup, cek KTP
        print("Boleh masuk")

#logical operator and
if umur >= 17 and punya_ktp:   # dua kondisi dicek sekaligus
    print("Boleh masuk")

""" === past statement ===
Pernyataan if tidak boleh kosong.
Tapi kalau karena suatu alasan kamu punya if tanpa isi,
bisa dengan menambahkan pass supaya tidak error."""

a = 10

if a > 5:
    pass   # tidak melakukan apa-apa, tapi biar tidak error

""" === pass in development ===
selama pengembangan program, seseorang ingin membuat kerangka/struktur program dulu sebelum mengisi detailnya.
jadi pernyataan pass memungkinkan melakukan itu tanpa error sintaks.
"""

menu = 1

if menu == 1:
    pass   # nanti isi fitur login
elif menu == 2:
    pass   # nanti isi fitur daftar
else:
    print("Menu tidak ada")
