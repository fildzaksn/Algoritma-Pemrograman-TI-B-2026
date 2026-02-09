#nama variabelnya sebaiknya tambah s, karna isi elemennya lebih dr satu
#
names = ["Fildza", "Rania", "Najwa"]
print(names)

#mengakses elemen array (pakai indeks)
print(names[1])

#len()

#looping
#ngeprint semua elemen secara terpisah
for nama in names:
    print(nama)

#append()

#removing array elements
names.pop(1)
print(names)

#kalau ga pakai parameter, yang hilang bakal elemen yg terakhir