"""Mengimplementasikan Quicksort di Python
#pivot : nilai patokan (batas)"""

def partition(array, low, high): #low = indeks paling rendah, high paling tinggi
  pivot = array[high]
  i = low - 1

  for j in range(low, high): #perulangan pertaman utk membagi daerah (bagian data yg kecil dan data yg nilainya besar)
     if array[j] <= pivot:
       i += 1 #ngitung bnyknya swap
       array[i], array[j] = array[j], array[i]

  array[i+1], array[high] = array[high], array[i+1]
  return i+1

def quicksort(array, low=0, high=None):
  if high is None:
    high = len(array) - 1

  if low < high:
    pivot_index = partition(array, low, high)
    quicksort(array, low, pivot_index-1)
    quicksort(array, pivot_index+1, high)

mylist = [64, 34, 25, 5, 22, 11, 90, 12]
quicksort(mylist)
print(mylist)
