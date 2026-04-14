"""Deskripsi: 
Buat versi OOP dari sistem pemesanan tiket bioskop menggunakan dua class sederhana. 
Ketentuan Program: 
1. Buat class Film dengan atribut judul dan harga, serta method tampilkan() yang mencetak 
informasi film dalam format: “Judul Film - Rp harga”. 
2. Buat class Transaksi dengan atribut total (awalnya 0) dan method tambah(film, jumlah) 
yang menambahkan harga ke total, serta method struk() yang menampilkan total 
pembelian. 
Halaman 4 dari 5 
Quiz 1 Praktikum Algoritma Pemrograman 
Universitas Riau 
3. Pada program utama, buat minimal 3 objek Film dan tampilkan semuanya menggunakan 
for loop. 
4. Buat satu objek Transaksi, minta pengguna memilih film dan jumlah tiketnya, lalu panggil 
method tambah() dan tampilkan struk akhir dengan method struk(). """

class Film:
    def __init__(self, judul, harga):
        pass