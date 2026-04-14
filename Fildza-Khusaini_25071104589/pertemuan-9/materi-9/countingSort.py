"""Implement Counting Sort in Python
"""

def countingSort(arr):
  max_val = max(arr)
  count = [0] * (max_val + 1) 
  #araay [0] dikali (blabla) untuk menciptakan list array yg bernama count yg berisi 0 semua, sebanyak 7 buah

  while len(arr) > 0:
    num = arr.pop(0)
    count[num] += 1

  for i in range(len(count)):
    while count[i] > 0:
      arr.append(i)
      count[i] -= 1

  return arr

mylist = [4, 2, 2, 6, 3, 3, 1, 6, 5, 2, 3]
mysortedlist = countingSort(mylist)
print(mysortedlist)
