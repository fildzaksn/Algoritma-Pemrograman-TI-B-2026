""" === the python match statement ===
digunakan untuk menjalankan aksi yang berbeda berdasarkan kondisi yang berbeda.
daripada menulis banyak if elif else, match akan memilih satu dari banyak blok kode untuk dijalankan. """

menu = 2
match menu:        #variabel yang mau di cek
    case 1:
        print("masuk")

    case 2:
        print("buat akun")

    case 3:
        print("keluar")

    case _:                     #default(else)
        print("menu tidak ada")

#ekspresi match dievaluasi satu kali.
#nilai dari ekspresi tersebut dibandingkan dengan nilai pada setiap case.
#jika ada yang cocok, blok kode yang terkait akan dijalankan.
#gunakan karakter (_) sebagai kasus terakhir agar blok kode dieksekusi ketika tidak ada kecocokan lain

""" 
=== combine values ===
karakter pipe | sebagai operator (or) dalam evaluasi case,
untuk mengecek lebih dari satu kemungkinan nilai dalam satu case
"""

tanggal = 16

match tanggal:
  case 11 | 12 | 13 | 14 | 15:      #jika tanggal bernilai 11 or 12 or 13 or 14 or 15
    print("bukan tanggal merah")    #bukan tanggal merah
  case 16 | 17:                     #jika tanggal bernilai 16 or 17
    print("ini tanggal merah!!")    #ini tanggal merah 


""" === if statements as guards === 
menambahkan pernyataan if di dalam evaluasi case sebagai pengecekan tambahan """

bulan = 2
tanggal = 16

match tanggal:
  case 15 | 16 | 17 if bulan == 2:      #15, 16, 17 adalah nilai dari 'tanggal'
    print("ada tanggal merah")          #jika tanggal dan jika kondisi bulan == 2 True, maka blok kode dijalankan
                                        #jika False, maka lanjut ke case berikutn
  case 15 | 16 | 17 if bulan == 5:      
    print("tidak ada tanggal merah")
    
  case _:
    print("nilai tidak valid")

