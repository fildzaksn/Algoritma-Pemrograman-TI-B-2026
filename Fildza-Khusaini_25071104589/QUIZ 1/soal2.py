"""Berdasarkan Soal 1 kembangan kode agar pelanggan dapat membeli tiket untuk lebih dari 
satu film (atau lebih dari satu jenis tiket) dan program menghitung total harga seluruh 
pembelian. 
Ketentuan Program: 
1. Gunakan while loop agar pelanggan dapat terus menambah pembelian tiket. Loop berhenti 
ketika pelanggan memasukkan angka 0. 
2. Simpan setiap pembelian ke dalam sebuah list berisi judul film dan jumlah tiket. 
3. Setelah selesai, tampilkan daftar pembelian menggunakan for loop beserta subtotal tiap 
item (harga tiket × jumlah tiket). 
4. Tampilkan total harga keseluruhan di bagian akhir."""

print(" === DAFTAR FILM === ")
list_film = { 1: ["Danur", 50000],
             2: ["Inside Out", 45000],
             3: ["Sore", 35000],
             4: ["KKN", 30000],
             5: ["Jumbo", 40000]}

angka = 1
for film in list_film.values():
    print(f"{angka}. {film}")
    angka += 1
print()



beli = []
y = 1

while y:
    nomor = int(input("Masukkan nomor film (ketik 0 untuk berhenti memesan): "))
    if nomor == 0:
        y = 0
    elif nomor < 0 or nomor >= 5:
            print("Nomor film tidak valid!")
    else:
        print(f"{list_film[nomor]}")
        beli.append(list_film[nomor])


print("=== DAFTAR PEMBELIAN ===")
for x in beli:
    total = sum(x[1])
    print(x)
    print(total)