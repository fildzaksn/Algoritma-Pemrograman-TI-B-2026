""" === python for loops ===
for = mengambil item satu per satu dari sequence
Bisa dipakai untuk list, tuple, set, dictionary, dan string.
"""
benda = ["pena", "meja", "kursi"]

for item in benda:  #setiap item akan berisi satu benda setiap satu pengulangan
    print(item)


"""=== looping through a string ===
string adalah objek yang dapat diiterasi, karna string berisi sebuah urutan karakter"""

kata = 'fildza'

for huruf in kata:  #setiap putaran, huruf berisi satu karakter
    print(huruf)


""" === break statement ===
dengan menggunakan statement break, kita dapat menghentikan loop sebelum melewati semua item"""

benda = ["pena", "meja", "kursi"]

for item in benda:  #setiap item akan berisi satu benda setiap satu pengulangan
    print(item)
    if (item) == "meja":    #jika item adalah 'meja', loop berhenti
        break 

#contoh jika loop berhenti ketika item adalah 'meja'
benda = ["pena", "meja", "kursi"]

for item in benda:  #setiap item akan berisi satu benda setiap satu pengulangan
    if (item) == "meja":    #jika item adalah 'meja', loop berhenti
        break 
    print(item)
#karena break berada di sebelum perintah print, jadi 'meja' tidak ikut dicetak

"""=== continue statement ===
menghentikan iterasi yang berjalan, kemudian lanjut ke iterasi berikutnya"""

kelas = [1, 2, 3, 4, 5, 6]

for x in kelas:
    if x == 4:      #jika x adalah 4, lanjut ke iterasi berikutnya
        continue
    print(x)

""" === range() function ===
fungsi range() melakukan perulangan pada sebuah blok kode sebanyak jumlah tertentu
fungsi range() mengembalikan sebuah urutan angka"""

for angka in range (4):
    print(angka)
#urutan angka yang dikembalikan defaultnya dimulai dari 0, lalu bertambah satu, dan berhenti di angka yang di tentukan

#menentukan nilai awal dengan menambahkan parameter
for angka in range(2, 4):    #range(start:stop)
    print(angka)

#menentukan nilai kenaikan
for x in range(3, 10, 2):        #range(start:stop:step)
    print(x)
#urutan angka akan dimulai dari 3, lalu bertambah 2, dan berhenti sebelum angka 10

""" === else in for loop ===
else pada perulangan for digunakan untuk menentukan sebuah blok kode yang akan dijalankan ketika perulangan selesai"""

for i in range(4):
    print(i)
else: 
    print("loop selesai")   #dicetak setelah loop selesai

#jika loop dihentikan (break)
for i in range(4):
    if i == 2: 
        break
    print(i)
else: 
    print("loop selesai")
#karna loop dihentikan (break), else tidak dijalankan

""" === nested loops ===
(loop yang ada di dalam loop)
loop bagian dalam (inner loop) akan dijalankan setiap outer loop melakukan satu perulangan"""

buah = ['apel', 'pisang', 'mangga']
warna = ["merah", "kuning", "hijau"]

for x in buah:      #outer loop (x akan berisi buah)
    for y in warna: #inner loop (y akan berisi warna)
        print(x, y)
        #cetak (nilai x dan y)

"""=== the pass statement ===
loop for tidak boleh kosong, 
jika ingin kosong loop for kosong, gunakan pass statement untuk menghindari error"""

for x in [1, 2, 3, 4]:
    pass
#jika for loop kosong tidak menggunakan statement pass, akan menimbulkan error

