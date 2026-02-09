#python function -> blok kode yang hanya dijalankan saat fungsi dipanggil
#fungsi dapat mengembalikan data sebagai hasil
#di python, fungsi didefinisikan dengan kata kunci def

def contoh_fungsi():
    print('ini contoh fungsi')

contoh_fungsi()   #memanggil fungsi contoh_fungsi

#definisi fungsi tidak boleh kosong, jadi gunakan pass statement untuk menghindari error
def contoh_fungsi2():
    pass

"""=== function arguments ===
# informasi (data) bisa dikirim ke dalam fungsi sebagai argument
# #argument ditulis setelah nama fungsi, di dalam tanda kurung ()"""

def cth_fungsi(tingkat):    #tingkat adalah parameter
    print(tingkat + " SMA")

#memanggil fungsi 
cth_fungsi("kelas satu")    #"kelas satu" adalah argument
cth_fungsi("kelas dua")
cth_fungsi("kelas tiga")
#parameter adalah variabel yang dituliskan di dalam tanda kurung pada pendefinisian fungsi
#argument adalah nilai sebenarnya yang dikirim ke fungsi saat fungsi tersebut dipanggil

""" === number of argument ===
jumlah argument saat pemanggilan harus sama dengan jumlah parameter di definisi fungsi"""

def tambah(a, b):   #a dan b adalah parameter
    print(a+b)

tambah(1, 2)    #2 dan 3 adalah argumet

"""=== default parameter values ===
parameter dapat diberikan nilai default"""

def cth_fungsi2(nama = "temanku"):  #nama  punya nilai default 'temanku'
    print("hai", nama)

cth_fungsi2("fildza")   #ada argumennya, jadi pakai argument
cth_fungsi2()   #tanpa argument, jadi pakai nilai deefault

"""=== keyword arguments ===
argument dapat dikirim menggunakan sintaks key = value"""

def peliharaan(hewan, nama):    #hewan dan nama adalah parameter
    print("aku punya", hewan)
    print("nama", hewan + "ku itu", nama)

#memanggil fungsi dengan keyword argument
peliharaan(hewan = "kucing", nama = "piyo")
#urutan argument boleh acak
peliharaan(nama = 'ciko', hewan = 'ayam')

"""=== positional arguments ===
ketika memanggil fungsi dengan argument tanpa menggunakan keyword, 
positional arguments harus berada dalam urutan yang benar"""

def peliharaan(hewan, nama):    #hewan dan nama adalah parameter
    print("aku punya", hewan)
    print("nama", hewan + "ku itu", nama)

#memanggil fungsi 
peliharaan("ayam", "jaki")
#jika urutannya tidak sesuai, hasilnya akan berubah
peliharaan("jaki", "ayam")


"""=== mixing positional and keyword arguments ===
yaitu menggabungkan positional dan keyword arguments saat memanggil fungsi.
positional arguments harus di tulis lebih dulu sebelum keyword arguments"""

def peliharaan(hewan, jenis, nama):    #hewan, jenis, dan nama adalah parameter
    print("aku punya", hewan + " jenis", jenis + ", ku beri nama", nama)

peliharaan("kucing", jenis = "persia", nama = "piyo")
#"kucing" adalah positional arguments, yang otomatis langsung masuk ke parameter hewan
#jenis = "persia" dan nama = piyo adalah keyword arguments

"""=== passing different data types ===
tipe data apapun bisa dikirim kedalam fungsi sebagai argument
tipe data tidak akan diubah saat argument dikirim ke fungsi"""

def jenis_hewan(nama):  #nama adalah list
    for hewan in nama:  #hewan adalah salah satu elemen dari list
        print(hewan)    #cetak elemen

nama_hewan = ["kucing", "ayam", "ikan"]
#memanggil fungsi dengan argument bertipe list
jenis_hewan(nama_hewan)

""" === return values === """

def tambah (a, b):
    return a + b

hasil = tambah(6, 3)
print(hasil)
#fungsi dapat mengembalikan nilai menggunakan statement return

def nama_hewan ():
    return ["kucing", "ayam"]

hewan = nama_hewan()
print(hewan)
#fungsi bisa mengembalikan data apapun, termasuk list, tuple dan lainnya

"""=== positional only arguments ===
parameter fungsi yang harus diisi berdasarkan posisi, tidak boleh pakai nama parameter
tandanya adalah simbol / di dalam definisi fungsi"""

def sapa(nama, /):
    print("haii", nama)

sapa("pija") #karna ada /, jadi cuma boleh dipanggil lewat posisi, bukan pakai keyword

"""=== keyword only arguments ===
parameter fungsi yang harus diisi pakai nama parameter (keyword), tidak boleh cuma berdasarkan posisi
tandanya adalah simbol * di dalam definisi fungsi"""

def sapa(*, nama):
    print("halo lagi", nama)

sapa(nama = "pija") #karna ada *, jadi argument 'nama' wajib dipanggil sebagai keyword

""" === combining positional only and keyword only ===
dalam sebuah fungsi kita bisa menggabungkan positional only (argument sebelum /) dan keyword only (argumen setelah *)"""

def biodata(nama, umur, /, *, kota, status):
    print(nama, umur, kota, status)

#memanggil fungsi
biodata("fildza", 18, kota = "pekanbaru", status = True )
#kota dan status wajib pakai keyword