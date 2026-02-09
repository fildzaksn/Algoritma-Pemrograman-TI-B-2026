"""Soal 2 (Range dan Pola Bilangan)
Buat sebuah fungsi bernama bilangan prima(n) yang:
1. Menggunakan range()
2. Mengembalikan list bilangan prima dari 1 sampai n
Kemudian:
1. Panggil fungsi untuk n = 50
2. Tampilkan hasilnya"""

def bilangan_prima(n):
    hasil = []
    for i in range(1, n + 1): #cek angka 1 sampai n, anggap dulu inni prima
        prima = True
       
        for pembagi in range (2, i):
           if i % pembagi == 0: #bagi i dengan semua angka sebelum dia, kalau habis dibagi berarti bukan prima
                prima = False
     
        if prima:
            hasil.append(i)

    return hasil                

print(bilangan_prima(50))
