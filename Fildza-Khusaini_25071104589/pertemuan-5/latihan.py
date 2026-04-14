# Diberikan dua matriks:
A = [[5, 3, 1],
    [2, 8, 4],
    [6, 0, 7]]

B = [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]
# Buatlah program python (tanpa NumPy) yang:
# a Menjumlahkan matriks A dan B, simpan hasilnya dalam variabel C_tambah
print("a.")

def tambah(A, B):
    baris, kolom, = len(A), len(A[0])
    hasil = [[A [i][j] + B[i][j] for j in range(kolom)] for i in range (baris)]
    return hasil

C_tambah = tambah(A, B)
for baris in C_tambah:
    print(baris)

print()
print("b.")      
# bMengurangkan matriks A dikurangi B, simpan dalam variabel C_kurang
def kurang(A, B):
   baris, kolom, = len(A), len(A[0])
   hasil = [[A [i][j] - B[i][j] for j in range(kolom)] for i in range (baris)]
   return hasil

C_kurang = kurang(A, B)
for baris in C_kurang:
    print(baris)

print()
print("c.")
# cMengalikan setiap elemen matriks A dengan skalar k = 4 , simpan dalam C_skalar
def kali(A, k):
    hasil = []
    for baris in A:
        baris_baru = [elemen * k for elemen in baris]
        hasil.append(baris_baru)
    return hasil

hasil = kali(A, 4)
for baris in hasil:
    print(baris)

# dMenampilkan ketiga hasil dengan format rapi baris per baris