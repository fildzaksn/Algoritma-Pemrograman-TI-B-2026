
"""Soal 3 (Rekursi - Penjumlahan Digit)
Buat sebuah fungsi rekursif bernama jumlah digit(n) yang:
1. Menghitung jumlah seluruh digit dari sebuah bilangan
2. Menggunakan konsep rekursi
Contoh:
Input: 1234
Output: 10"""

def jumlah_digit(n):
    if n < 10:  #kalau tinggal 1 digit, return n
        return n
    else:
        return n % 10 + jumlah_digit(n // 10)   #ambil digit terakhir + digit terakhir tadi dibuang
         

print(jumlah_digit(1234))
