"""
Buatlah sebuah program yang mengimplementasikan Linear dan Binary Search.
Tampilkan data dan minta pengguna untuk memasukkan nilai berapa yang dicari, jika ketemu maka tampilkan index nya, jika tidak maka return -1.
"""

# linear search
print('=== DAFTAR NILAI ===')
data = [59, 40, 36, 40, 30, 26, 97, 8, 23, 31, 2, 40, 99, 70, 64, 36, 43, 20, 1, 9]
print(data)

def LinearSearch(daftar_nilai, nilai_dicari):
    for i in range(len(daftar_nilai)):
        if daftar_nilai[i] == nilai_dicari:
            return i
    return -1

nilai = int(input('Masukkan nilai yang ingin dicari: '))

hasil = LinearSearch(data, nilai)
if hasil != -1:
    print('Nilai ditemukan pada indeks ke-', hasil)
else:
    print('nilai tidak ditemukan')

print()

#binary search
print('=== DAFTAR NILAI ===')
data = [59, 40, 36, 40, 30, 26, 97, 8, 23, 31, 2, 40, 99, 70, 64, 36, 43, 20, 1, 9]

n = len(data)
for i in range(n-1):
  for j in range(n-i-1):
    if data[j] > data[j+1]:
      data[j], data[j+1] = data[j+1], data[j]

print('nilai yang telah diurutkan:', data)

def BinarySearch(list_nilai, cari_nilai):
    left = 0
    right = len(list_nilai) - 1

    while left <= right:
        mid = (left + right) // 2

        if list_nilai[mid] == cari_nilai:
            return mid
        if list_nilai[mid] < cari_nilai:
            left = mid + 1
        else:
            right = mid - 1
    return -1

angka = int(input('Masukkan nilai yang ingin dicari: '))

cari = BinarySearch(data, angka)
if cari != -1:
    print('Nilai ditemukan pada indeks ke-', cari)
else:
    print('nilai tidak ditemukan')