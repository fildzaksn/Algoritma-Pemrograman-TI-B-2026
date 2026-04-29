"""Buatlah sebuah program Python yang berjalan di terminal dengan ketentuan sebagai berikut:

Program meminta pengguna untuk memasukkan jumlah elemen yang akan dimasukkan ke dalam array.
Selanjutnya, pengguna memasukkan sejumlah bilangan bulat non-negatif sesuai jumlah yang telah ditentukan, satu per satu.
Setelah semua elemen dimasukkan, program akan mengurutkan array tersebut menggunakan dua algoritma pengurutan,
yaitu Radix Sort dan Merge Sort,secara terpisah.
Program menampilkan hasil pengurutan dari masing-masing algoritma ke layar terminal.
Input yang diterima hanya bilangan bulat non-negatif (≥ 0). Program harus menangani input yang tidak valid.
Implementasikan fungsi terpisah untuk Radix Sort dan Merge Sort.
Tampilkan array sebelum dan sesudah diurutkan untuk setiap algoritma.
"""
#radix sort
n = int(input('Masukkan jumlah elemen: '))

data = []
for i in range(n):
    angka = int(input('Masukkan angka: '))
    if angka <= 0 or angka is float:
        print('bilangan harus bulat non negatif')
    else:
        data.append(angka)
print("Daftar bilangan awal:", data)

radiks_array = [[], [], [], [], [], [], [], [], [], []]
nilai_maks = max(data)

def radix_sort():
    exp = 1

    while nilai_maks // exp > 0:
        while len(data) > 0:
            nilai = data.pop()
            radiks_indeks = (nilai // exp) % 10
            radiks_array[radiks_indeks].append(nilai)

        for j in radiks_array:
            while len(j) > 0:
                nilai = j.pop()
                data.append(nilai)

        exp *= 10

radix_sort()
print('setelah diurutkan (radix):', data)
print()

#merge sort
def merge_sort(data):
    if len(data) <= 1:
        return data
    
    mid = len(data) // 2
    leftHalf = data[:mid]
    rightHalf = data[mid:]

    sortedLeft = merge_sort(leftHalf)
    sortedRight = merge_sort(rightHalf)
    return merge(sortedLeft, sortedRight)

def merge(left, right):
    hasil = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            hasil.append(left[i])
            i += 1
        else:
            hasil.append(right[j])
            j += 1
    
    hasil.extend(left[i:])
    hasil.extend(right[j:])
    return hasil

tes = merge_sort(data)
print('Setelah diurutkan(merge):', tes)