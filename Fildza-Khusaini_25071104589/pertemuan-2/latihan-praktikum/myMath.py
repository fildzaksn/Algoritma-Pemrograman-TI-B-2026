#1
def tambah(a, b):
    return a + b

#2
def kurang(a, b):
    return a - b

#3
def kali(a, b):
    return a * b

#4
def bagi(a, b):
    if b == 0:
        print("Pembagian tidak dapat dilakukan karena pembagi bernilai 0")
    else:
        return a / b
    
#5
def modulus(a, b):
    return a % b

#6
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1), fibonacci(n - 2)
