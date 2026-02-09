"""Soal 3 (Rekursi - Penjumlahan Digit)
Buat sebuah fungsi rekursif bernama jumlah digit(n) yang:
1. Menghitung jumlah seluruh digit dari sebuah bilangan
2. Menggunakan konsep rekursi
Contoh:
Input: 1234
Output: 10"""

def jumlah_digit(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n + jumlah_digit(n)
    
print(jumlah_digit(1234))