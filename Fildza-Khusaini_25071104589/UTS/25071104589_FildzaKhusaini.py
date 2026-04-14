# === BAGIAN A ===.
DAFTAR_ANGKA = [23, 67, 4, 89, 15, 42, 73, 31, 58, 9] 

def tebak_angka(angka_rahasia, maks_percobaan = 7):
    percobaan = 0
    while percobaan < maks_percobaan: #jalankan program selama kesempatan percobaan < 7
        angka = int(input('Input tebakan angka: '))
        
        if angka < angka_rahasia: #jika angka yang ditebak lebih kecil dari angka rahasia
            print('Terlalu kecil')
            continue

        elif angka > angka_rahasia: #jika angka yang di input lebih besar dari angka rahasia
            print('Terlalu besar')
            continue

        else: #jika angka yang diinput sama dengan angka rahasia
            print('Benar!')
            sisa_percobaan = maks_percobaan - (percobaan + 1)

        if sisa_percobaan == 0:
            return False
        else:
            return True
        break #hentikan perulangan jika pemain berhasil 
        
def hitung_skor_berhasil(berhasil, sisa_percobaan):
    if berhasil == True: #jika pemain berhasil menebak angka rahasia
        skor = sisa_percobaan * 10 #kalikan sisa percobaan dengan 10 untuk menghitung skor
        return skor
    else: #jika pemain gagal menebak angka rahasia sama sekali
        return 0        

def main_satu_ronde(nama, nomor_ronde = 0):
    for i in range(nomor_ronde):
        nomor_ronde[i] = DAFTAR_ANGKA[i] #ambil angka dari daftar angka dengan urutan yang sesuai dengan nomor ronde

    main = tebak_angka(main_satu_ronde)
    skor = hitung_skor_berhasil(tebak_angka)


# === BAGIAN B ===
def tampilkan_riwayat(riwayat):
    riwayat = [] #list kosong untuk menampung riwayat permainan

    if len(riwayat) == 0: #jika isi list riwayat kosong 
        return('Belum ada riwayat')
    else:
        for i in (len(riwayat)):
            no = 1
            for j in (len(riwayat[0])):
                print(f'No: {no}. | Nama: {riwayat['nama']} | Skor: {riwayat['skor']}')
            no+=1


# === BAGIAN C ===
def selection_sort_riwayat(riwayat):
    n = len(riwayat)
    data = riwayat.copy() #salinan list riwayat

    for i in range(n - 1):
        maks_indeks = i #inisialisasi maks_indeks dengan elemen ke i
        for j in range(i+1, n):
            if data [j][1] > maks_indeks: #jika skor data ke j lebih besar dari skor awal
                maks_indeks = data[j][1]
    return data

def tampilkan_leaderboard(riwayat):
    urutan = selection_sort_riwayat(riwayat)


# ==== PROGRAM UTAMA ====
nama = input("Masukkan nama pemain: ")
main = main_satu_ronde(nama)
