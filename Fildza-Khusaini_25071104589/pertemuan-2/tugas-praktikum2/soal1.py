"""
Soal 1 (Function dan Validasi Data)
Buat sebuah fungsi bernama rata rata(nilai) yang:
1. Menerima sebuah list berisi nilai mahasiswa
2. Menghitung rata-rata nilai
3. Jika list kosong, kembalikan pesan: "Data kosong"
Kemudian:
1. Panggil fungsi dengan list: [80, 75, 90, 60, 85]
2. Tampilkan hasilnya
"""

def rata_rata(nilai):
    if len(nilai) == 0:
        return ("Data kosong")
    else:
        total = 0
        jumlah =0
        for i in nilai:
            total += i
            jumlah += 1
        rata = total / jumlah
    return(rata)

data = [80, 75, 90, 60, 85]
hasil = rata_rata(data)
print("Rata rata nilai adalah", hasil)
