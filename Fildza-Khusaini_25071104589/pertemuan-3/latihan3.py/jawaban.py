import myOOP

"""
==================================================
A. INHERITANCE (Pewarisan)
==================================================
"""
y = myOOP.ProdukElektronik("TV", "300.000", 2)
y.info_produk()   

x = myOOP.ProdukMakanan("Roti", "15.000", "12-12-2026")
x.info_produk()

'''
==================================================
B. POLYMORPHISM
==================================================
'''
a = myOOP.Email("Pesan baru")
a.kirim()

b = myOOP.SMS("Pesan baru")
b.kirim()

"""
==================================================
C. ENCAPSULATION
==================================================
"""
mhs1 = myOOP.Mahasiswa()
mhs2 = myOOP.Mahasiswa()

print(mhs1.set_nilai(90))
print(mhs1.get_nilai())
print(mhs2.set_nilai(-10))
print(mhs2.get_nilai())