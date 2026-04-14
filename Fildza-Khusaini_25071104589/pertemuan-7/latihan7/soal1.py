"""Diberikan list berikut:

python data = [ 918, 336, 637, 814, 507, 685, 854, 933, 970, 461, 26, 884, 684, 47, 922, 246, 431, 985, 412, 679, 708, 354, 369, 396, 406, 882, 119, 682, 378, 578, 208, 899, 344, 436, 153, 835, 836, 985, 117, 619, 225, 345, 210, 606, 313, 998, 681, 989, 212, 163, 762, 389, 906, 423, 204, 627, 430, 568, 430, 71, 429, 492, 817, 577, 621, 914, 500, 783, 872, 992, 498, 477, 34, 570, 113, 2, 58, 844, 464, 293, 302, 183, 711, 777, 71, 441, 261, 713, 544, 528, 759, 193, 163, 272, 389, 979, 608, 977, 721, 508, 619, 875, 948, 750, 991, 711, 855, 111, 555, 608, 535, 603, 538, 753, 190, 441, 85, 200, 193, 577, 774, 578, 405, 306, 256, 926, 433, 444, 459, 368, 187, 671, 701, 714, 411, 940, 603, 736, 665, 947, 517, 19, 365, 165, 514, 133, 491, 642, 636, 957]

Kerjakan semua poin di bawah ini:

1. Implementasikan Bubble Sort untuk mengurutkan data dari kecil ke besar. Gunakan versi yang dioptimasi dengan flag swapped agar algoritma berhenti lebih awal jika array sudah terurut.
2. Implementasikan Selection Sort untuk mengurutkan data dari besar ke kecil.
3. Hitung berapa kali pertukaran (swap) terjadi pada masing-masing algoritma. Tampilkan jumlahnya.
4. Jalankan kedua algoritma pada list data yang sama persis (jangan gunakan hasil sort sebelumnya sebagai input).

---
Output yang Diharapkan

```
Bubble Sort (kecil → besar): 
Jumlah swap Bubble Sort: ...

Selection Sort (besar → kecil): 
Jumlah swap Selection Sort: ...
```"""
python_data = [ 918, 336, 637, 814, 507, 685, 854, 933, 970, 461, 26, 884, 684, 47, 922, 246, 431, 985, 412, 679, 708, 354, 369, 396, 406, 882, 119, 682, 378, 578, 208, 899, 344, 436, 153, 835, 836, 985, 117, 619, 225, 345, 210, 606, 313, 998, 681, 989, 212, 163, 762, 389, 906, 423, 204, 627, 430, 568, 430, 71, 429, 492, 817, 577, 621, 914, 500, 783, 872, 992, 498, 477, 34, 570, 113, 2, 58, 844, 464, 293, 302, 183, 711, 777, 71, 441, 261, 713, 544, 528, 759, 193, 163, 272, 389, 979, 608, 977, 721, 508, 619, 875, 948, 750, 991, 711, 855, 111, 555, 608, 535, 603, 538, 753, 190, 441, 85, 200, 193, 577, 774, 578, 405, 306, 256, 926, 433, 444, 459, 368, 187, 671, 701, 714, 411, 940, 603, 736, 665, 947, 517, 19, 365, 165, 514, 133, 491, 642, 636, 957]

print("Soal 1")
n = len(python_data)
swapped = False
counter1 = 0


for i in range(n-1):
    for j in range(n-i-1):
        if python_data[j] > python_data[j +1]:
            python_data[j], python_data[j +1] = python_data[j +1], python_data[j]
            swapped = True 
            counter1 += 1

        if not swapped:
            break 

print("Urutan dari kecil ke besar: ", python_data)
print("banyak swap:", counter1)


print()
print("soal 2")
n = len(python_data)
counter = 0

for i in range(n):
    min_index = i
    for j in range(i+1, n):
        if python_data[j] > python_data[min_index]:
            counter += 1
            min_index = j
    python_data[i], python_data[min_index] = python_data[min_index], python_data[i]

print("Urutan dari besar ke kecil:", python_data)
print("Banyak swap:" ,counter)