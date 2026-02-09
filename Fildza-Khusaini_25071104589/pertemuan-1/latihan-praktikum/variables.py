'''
variabel -> wadah untuk menyimpan nilai data
Di python, variabel dibuat saat kita mengisi nilai ke dalamnya, 
tapi python tidak memiliki perintah untuk mendeklarasikan variabel.
Tidak perlu mendeklarasikan tipe data ketika menuliskan variabel.
variabel python -> variabel legal dan variabel non-legal
'''
# 
# ======== VARIABEL LEGAL (cara penamaan variabel yang benar) ========
#1
jumlah = 10             
''' menggunakan huruf kecil semua '''

#2
jumlah1 = 10
''' meletakkan angka di akhir kalimat tanpa menggunakan spasi'''

#3
Jumlah = 10
''' menggunakan kapital di awal '''

#4
JUMLAH = 10
''' menggunakan huruf kapital untuk semua huruf'''

#5
_jumlah = 10
''' menggunakan simbol _ di bagian awal variabel'''

#6
jumlahAngka = 10
''' menggunakan huruf kapital untuk memisahkan antar suku kata'''

#7
jumlah_angka = 10
''' menggunakan _ untuk memisahkan antar suku kata'''

# =========== VARIABEL NON LEGAL (cara penamaan variabel yang salah) ===========

# 1jumlah = 10
''' penamaan variabel diawali dengan angka '''

# @jumlah = 10
''' menggunakan simbol (@#$%-) selain underscore (_)'''

#jumlah angka = 10
''' menggunakan spasi sebagai pemisah antar suku kata '''


# ============================= CASE SENSITIVE ==============================
""" nama variabel sensitif terhadap besar-kecilnya huruf """

nama = 'fildza'
NAMA = 'fildza khusaini'
"""ketika mencetak variabel nama, hasilnya akan berbeda apabila kita mencetak variabel NAMA """

# ====== MANY VALUES to MULTIPLE VARIABLES (mengisi nilai ke bbrp variabel dlm satu baris) ======

nama, kelas, nim = 'fildza', 'tib', 25071104589

print(nama)
print(kelas)
print(nim)

# === ONE VALUE to MULTIPLE VARIABLES (mengisi nilai yang sama ke bbrp variabel dalam satu baris)===

a = b = c = 'huruf'

print(a)
print(b)
print(c)

# CASTING - CASE 
# (mengubah tipe data suatu variabel dengan casting (akan dijelaskan lebih lanjut dibagian casting.py))

bilangan = 12
print(type(bilangan)) # <class 'int'>

bilangan = str(12)
print(type(bilangan)) # akan berubah menjadi '12'
                      #<class 'str'>

# UNPACK COLLECTION 
# (fitur python yg memungkinkan kumpulan nilai dalam list dsb diekstrak dan disimpan ke bbrp variabel sekaligus)

nama = ['fildza', 'rania', 'najwa']
a, b, c = nama

print(a)
print(b)
print(c)

""" OUTPUT VARIABLES """
# fungsi print() sering digunakan untuk mencetak variabel)
# fungsi print() dapat mencetak beberapa variabel dengan sekaligus, dengan memisahkan variabel dengan tanda (,) 
# bisa juga dengan tanda (+), akan tetapi gunakan spasi di akhir nilai variabel untuk memisahkan antar suku kata

a = 'teman-teman  '
b = 'semangat '
c = 'ya!'

print(a, b, c)

''' NOTES: # untuk nilai variabel yg bertipe numbers, tanda (+) akan bekerja sebagai operator aritmatika
           # dalam fungsi print(), jika menggabungkan string dan numbers menggunakan operator (+) akan menghasilkan error
           # jadi lebih baik pakai (,) aja daripada (+) '''

# =========== GLOBAL VARIABLES ============
'''
variabel yang dibuat diluar fungsi disebut variabel global
variabel global dapat digunakan baik di luar maupun di dalam fungsi 
contoh variabel global terdapat pada contoh-contoh di atas
sedangkan variabel yang dibuat di dalam fungsi, disebut variabel lokal
dan hanya bisa digunakan di dalam bagian fungsi saja
'''
    #contoh
kata = 'malas belajar'      
#kata di sini adalah variabel global

def kalimat():
    kata = 'belajarnya!'    
    #kata di sini adalah variabel lokal, karena letaknya didalam fungsi dan hanya bisa digunakan di dalam fungsi
    print('semangat', kata)

kalimat()                   
#memanggil fungsi kalimat()

print('jangan', kata)      
#di sini fungsi print() akan mencetak kata dari variabel global

    #contoh.2
#bisa juga menggunakan keyword 'global' kalau ingin mengubah variabel di dalam fungsi
nama = 'fildza'

def panggilan():
    global nama     
    nama = 'pija'

panggilan()
print('nama panggilanku', nama)