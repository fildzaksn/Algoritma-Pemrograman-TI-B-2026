def total_elemen(matriks): 
    total = 0 
    for baris in matriks: 
        for elemen in baris: 
            total += elemen 
    return total 
 
matriks = [[1, 2, 3], 
           [4, 5, 6], 
           [7, 8, 9]] 
 
print('Total manual:', total_elemen(matriks))