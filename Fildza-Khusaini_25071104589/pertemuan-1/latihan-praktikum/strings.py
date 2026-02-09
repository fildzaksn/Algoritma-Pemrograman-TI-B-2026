"""
string di dalam python diapit oleh tanda petik tunggal ('') atau petik ganda ("")
untuk menampilkan string dapat menggunakan fungsi print()
"""
#contoh
print("Hai semuanya, namaku Fildza")

''' ===== QUOTES INSIDE QUOTES ===== '''
#jika string mengandung tanda petik, maka tanda petik yang mengelilingi string harus berbeda.
print("Hari ini adalah hari jum'at")
print('aku memiliki kucing yang bernama "piyo"')


''' ===== ASSIGN STRING to A VARIABLE ===== '''
#string dapat disimpan ke dalam sebuah variabel menggunakan tanda (=)
nama = "nct dream"
print(nama)

kalimat = '''haii
hari ini hari kamis,
tanggal 29 januari 2026.'''
#string multiline bisa juga disimpan kedalam variabel menggunakan tiga tanda petik


''' === STRING ARE ARRAYS === 
string di Python merupakan kumpulan karakter Unicode. 
python tidak memiliki tipe data karakter terpisah, 
sehingga satu karakter dianggap sebagai string dengan panjang 1. 
Karakter dalam string dapat diakses menggunakan tanda kurung siku'''

nama = "cravity"
print(nama[0])


''' === LOOPING THROUGH A STRING === 
karna string adalah array, 
jadi kita dapat mengulangi (mengakses) setiap karakter dalam sebuah string menggunakan loop for
'''
#aturannya: for (variabel) in (iterable):

for x in 'nct dream':
    print(x)


''' === STRING LENGTH === 
untuk mencari panjang string pakai fungsi len()
'''

y = 'enhypen'
print(len(y))


''' === CHECK STRING === 
untuk mengecek apakah suatu karakter tertentu terdapat di dalam string atau tidak, 
gunakan keyword in
'''
#1
teks = 'life is but a dream'
print('but' in teks)                    
#mengecek apakah kata 'but' terdapat dalam string

#2
lirik = 'we got history'
if 'history' in lirik:
    print('benar, ada kata history')    
#contoh jika menggunakan pernyataan if 

#3
lirik = 'hate this distance'
print('this' not in lirik)              
#mengecek apakah kata 'this' tidak ada di dalam string

#4
lirik = 'hate distance'
if 'this' not in lirik:
    print("kata 'this' tidak ada di dalam lirik")   
#jika menggunnakan pernyataan if


''' === SLICING === 
mengambil rentang karakter dari sebuah string menggunakan syntax slicing.
tentukan indeks awal dan indeks akhir yang dipisah kan (;) untuk mengambil sebagian dari string '''

#slice from the start
lirik = "let me hold on to you"
print(lirik[:3])
#jika tidak menyertakan indeks awal, rentang akan dimulai dari karakter pertama

#slice to the end
lirik = "i've been the archer"
print(lirik[5:])
#jika tidak menyertakan indeks akhir, rentang akan mencakup hingga akhir

#negative idexing
lirik = "who could stay"
print(lirik[-10: -6])
#indeks negatif untuk memulai potongan dari akhir string
#indeks -1 dimulai dari karakter 'y.
#jadi -10 berada di karakter 'c', dan -6 karakter 'd', tetapi karakter 'd' tidak termasuk (eksklusif)


''' MODIFY STRINGS '''
#uppercase
lirik = 'easy they come'
print(lirik.upper())
#upper() -> mengubah string menjadi huruf kapital semua

#lowercase
lirik = 'EASY THEY GO'
print(lirik.lower())
#lower() -> mengubah string menjadi huruf kecil semua

#remove whitespace
lirik = "     who could stay    "
print(lirik.strip())
#strip() -> menghapus whitespace pada bagian awal dan akhir string

lirik = "whowhoicould staywhowho"
print(lirik.strip("who"))
#bisa juga untuk menghilangkan karakter selain whitespace

#replace string (mengganti elemen string)
kata = "about you"
print(kata.replace("a", "b"))
#karakter 'a' di dalam string diganti menjadi 'b'

#split string
kata = 'i never grew up'
print(kata.split())
#metode split() bertujuan untuk memisahkan kata atau substring berdasarkan delimiter

#string concatenation (menggabungkan dua string)
nama1 = 'nct'
nama2 = '127'
hasil = nama1 + nama2
# tanda (+) digunakan untuk menggabungkan dua string
print(hasil)

#untuk menambahkan spasi diantara dua string, tambahkan " "
hasil2 = nama1 + " " + nama2
print(hasil2)


""" === STRING FORMAT === """
#f-string (memformat string dengan menuliskan variabel langsung di dalam string menggunakan {})
angka = 30
print(f"hari ini tanggal {angka}")
#untuk membuat string menjadi f-string, tambahkan f di depan string literal

""" placeholders and modifiers """
#placeholder = wadah di dalam string untuk menampilkan nilai
#placeholders dapat diisi dengan variabel, operasi, fungsi, dan modifier untuk mengatur format nilai yang ditampilkan

angka = 20
print(f"suhu hari ini {angka} derajat")

''' NOTES: placeholder bisa menyertakan modifier untuk memformat nilai
dengan menambahkan (:), lalu diikuti dengan format yang valid'''

print(f"suhu hari ini {angka:.2f} derajat")
#setelah (:) terdapat format .2f yang berarti bilangan desimal dengan dua angka di belakang koma

#placeholder juga bisa berisi kode python, misalnya operasi aritmatika
print(f"suhu hari ini {6 * 5} derajat")


""" === ESCAPE CHARACTER ====
escape character digunakan untuk menyisipkan karakter khusus kedalam string dengan diawali tanda \ (backslash) """

#contoh = "aku sudah membaca novel "bulan" hari ini"
''' 
contoh di atas akan menghasilkan error.
petik dua di dalam string akan dianggap sebagai karakter ilegal karena, string juga diapit oleh petik dua
'''

contoh_benar = "aku sudah membaca novel \"bulan\" tadi malam"
#dengan menambahkan tanda (\), maka petik dua di dalam string tidak akan menjadi karakter ilegal

#contoh escape characters lainnya yang dapat digunakan di dalam python diantaranya:
kata1 = 'i\'ve been archer' #petik tunggal 
kata2 = 'hai\nsemuanya'     #new line 
kata3 = 'nct\rdream'        #carriage return (ngembaliin posisi kursor ke awal baris tanpa buat baris baru)
kata4 = 'halooo\tsemua'     #tab
kata5 = 'halo \bjuga'       #backspace


""" === STRING METHODS === 
methods nya ada banyak, +- 45 methods.
diantaranya itu ada:
    lower() untuk mengubah string jadi huruf kecil

    upper() untuk mengubah string jadi huruf besar

    capitalize() untuk huruf pertama jadi besar

    title() untuk huruf pertama tiap kata jadi besar

    strip() untuk menghapus spasi kiri & kanan
"""

