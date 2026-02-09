""" === while loop ===
pernyataan akan dijalankan selama kondisi benar 
"""
i = 5

while i < 7:        #selama i lebih kecil nilainya dari 7, maka cetak pesan 
    print('semangat belajarnya ya')
    i += 1

''' === break statement === 
dengan pernyataan break, kita dapat menghentikan loop meskipun kondisi while masih benar '''
i = 4

while i < 10:
    print('yok belajar lagi')
    if i == 7:      #jika i sama dengan 7, maka hentikan loop
        break
    i += 1

''' === the else statement ===
dengan pernyataan else, kita dapat menjalankan sebuah blok kode satu kali ketika kondisi sudah tidak bernilai benar lagi
 '''
i = 11

while i < 10:
    print('yok belajar lagi')
    i += 1
else :
    print('i lebih dari 10')
