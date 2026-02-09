"""
Soal 4 (Perulangan)
Buat sebuah program Python yang:
1. Menggunakan perulangan for
2. Menampilkan bilangan dari 1 sampai 10
3. Menghitung dan menampilkan jumlah dari bilangan 1 sampai 10
"""

total = 0   #menyimpan hasil penjumlahan semua angka

for angka in range(1, 11):  #perulangan dari 1 sampai 10
    print(angka)
    total+=angka    #tambahkan ke total setiap perulangan

print("Jumlah =", total)

