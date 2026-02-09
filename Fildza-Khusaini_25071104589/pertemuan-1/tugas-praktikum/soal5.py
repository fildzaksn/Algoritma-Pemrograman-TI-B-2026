"""
Soal 5 (Fungsi)
Buat sebuah fungsi bernama hitung(a, b) yang:
1. Menerima dua parameter a dan b
2. Mengembalikan hasil penjumlahan a + b
3. Mengembalikan hasil pengurangan a - b
Kemudian:
1. Panggil fungsi tersebut
2. Tampilkan hasil penjumlahan dan pengurangannya ke layar
Contoh keluaran:
Penjumlahan = 8
Pengurangan = 2
"""

def hitung(a, b):
    jumlah = a + b
    kurang = a - b
    return jumlah, kurang 

#memanggil fungsi
hasil_jumlah, hasil_kurang = hitung(9, 7)

print("Penjumlahan =", hasil_jumlah)
print("Pengurangan =", hasil_kurang)
