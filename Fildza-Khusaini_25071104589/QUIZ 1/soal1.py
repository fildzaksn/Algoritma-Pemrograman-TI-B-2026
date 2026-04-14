"""Ketentuan Program: 
1. Buat list film berisi 5 item film beserta harga tiketnya, contoh: [[ "Danur", 50000 ], [ 
"Inside Out 2", 45000 ], ...]. 
2. Tampilkan seluruh daftar film beserta harga menggunakan for loop dengan penomoran. 
3. Minta pengguna memasukkan nomor film yang dipilih. 
4. Gunakan if-else untuk memvalidasi input: jika nomor tidak valid, tampilkan pesan error; 
jika valid, tampilkan judul film dan harga tiket film yang dipilih.
"""
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

nomor = int(input("Masukkan nomor film (1-5): "))
if nomor < 1 or nomor > 6:
    print("Nomor film tidak valid!")
else:
    print(f"{list_film[nomor]}")