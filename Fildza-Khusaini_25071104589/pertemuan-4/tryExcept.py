#1
try:
    print(nama)
except:
    print("Terdapat kesalahan dalam program")

#2
try:
    print("nilai")
except:
    print("Terdapat kesalahan dalam program")
finally:
    print("Try-except selesai")

#3
try:
    jumlah = 5 + "10"
except TypeError:
    print("Terjadi kesalahan, pastikan anda menjumlahkan dua angka")
except:
     print("terjadi kesalahan lain")
#output

#4
try:
    tambah = 5 + "5"
except TypeError as e:
    print("Terjadi kesalahan,", e)

#5
try:
    print("nilai")
except:
    print("Terdapat kesalahan dalam program")
else:
    print("Tidak ada kesalahan")

#6
try:
    print("Hai")
except:
    print("Terdapat kesalahan dalam program")
finally:
    print("Try-except selesai")

#7
umur = -2

if umur < 0:
        raise Exception("umur tidak boleh negatif")

#8
nilai = "nol"

if not type(nilai) is int:
        raise TypeError("only integers are allowed")

#user input
nama = input("Masukkan nama: ")
print(f"Hai namaku {nama}")


angka = int(input("Masukkan angka: "))
print(f"sekarang ada {angka} anggota nct")

#validate input
y = True
while y == True:
    ipk = input("Masukkan ipk: ")
    try:
        ipk = float(ipk)
        y = False
    except:
        print("Input salah, silahkan coba lagi")

print("Input selesai")
