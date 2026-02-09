'''
Fungsi print() bisa digunakan untuk menampilkan teks atau output.
Kita bisa memanggil fungsi print() sebanyak yang diinginkan,
setiap panggilan akan mencetak teks di baris baru secara default.
Teks/string di python harus pakai tanda petik (quote), bisa pakai single atau double quote.
'''

#python output (print text)================================================================

nama = 'fildza' 
#variabel nama yang berisi string

#1              
print("halo, nama saya " + nama) 
#mencetak teks dengan cara menggabungkan string dan variabel (nama) bertipe string menggunakan tanda +

#2 
print(f'halo, nama saya {nama}') 
#mencetak teks dengan memasukkan variabel (nama) langsung ke dalam string menggunakan f-string

#3 
print("halo", nama)              
#mencetak teks dan variabel sekaligus, dipisahkan koma sehingga otomatis terdapat spasi


#4 contoh (f-string)
teman1 = 'Rania'
teman2 = 'Najwa'

print(f'Aku memiliki teman yang bernama {teman1} dan {teman2}')

#5 
'''
secara default, fungsi print() diakhiri dengan baris baru,
jika ingin mencetak beberapa kata di baris yang sama bisa pakai parameter end 
'''
print('Namaku fildza, kelas tib ', end="")
print('angkatan 2025 di UNRI')

#python output (print numbers)=========================================================
'''
fungsi print() juga bisa dipakai untuk menampilkan angka.
Berbeda dengan string, angka tidak perlu menggunakan single atau double quotes
'''

#contoh
print(127)
print(127.9)

#di dalam fungsi print juga bisa melakukan operasi aritmatika
print(1+2)
print(1*2)

#mix text and numbers
print('halo', 'umurku', 18, "tahun")
#bisa juga menggabungkan teks dan angka dalam satu output dengan memisahkannya menggunakan koma

#contoh mix text and numbers menggunakan f-string
tanggal = 28
bulan = 'januari'
tahun = 2026

print(f"Hari ini {tanggal} {bulan} {tahun}")

