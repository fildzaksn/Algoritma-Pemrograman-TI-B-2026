#studi kasus
#memesan donat
"""1. tampilkan daftar pilihan
2. meminta pilihan rasa donat
4. minta jumlah
5. tampilkan pesan"""

print("Selamat datang di Rumah Donat")
print("=== Varian Rasa ===")
print("1. coklat     5000")
print("2. strawberry 6000")
print("3. matcha     8000")
print("4. original   3000")

try:
    rasa = int(input("Pilih varian (1-4): "))
    jumlah = int(input("Jumlah: "))

    if rasa == 1:
        harga = 5000
        nama  = "donat coklat"
    elif rasa == 2:
        harga = 6000
        nama = "donat strawberry"
    elif rasa == 3:
        harga = 8000
        nama = "donat matcha"
    elif rasa == 4:
        harga = 3000
        nama = "donat original"
    else: #jika pilihan yang diinput tidak tersedia, buat exception
        raise ValueError("pilihan anda tidak tersedia")
         
    total = harga * jumlah

except ValueError as e: 
    print("Terjadi kesalahan,", e)

else:
    print("\n=== Pesanan anda ===\n")
    print("Varian:", nama)
    print("Jumlah:", jumlah)
    print("Total harga:", total)

finally:
    print("Terima kasih sudah memesan")