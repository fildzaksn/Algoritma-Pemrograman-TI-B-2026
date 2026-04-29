struktur = {
    "Skripsi_Aqil": {
        "Bab_1": {
            "pendahuluan.docx": 45,
            "latar_belakang.docx": 62
        },

        "Bab_2": {
            "landasan_teori.docx": 118,
            "referensi": {
            "paper_A.pdf": 340,
            "paper_B.pdf": 210
            }
        },

        "Bab_3": {
            "metodologi.docx": 89,
            "diagram": {
            "flowchart.png": 512,
            "erd.png": 278,
            "arsitektur": {
            "sistem.png": 430
            }
            }
        },

        "sidang": {
            "presentasi.pptx": 2048,
            "catatan_revisi.txt": 15
            },
            
    "README.txt": 8
    }
}

'''
Tugas A — Hitung Total Ukuran
Kamu ingin tahu berapa total ukuran_kb (KB) seluruh file dalam folder skripsimu,
termasuk file yang ada di dalam subfolder manapun.
'''
print()
def total_ukuran(folder: dict) -> int:
    total = 0
    for item in folder.values():
        if type(item) == dict: # cek folder atau bukan
            total += total_ukuran(item)
        else: # kalau file
            total += item
    
    return total

ukuran_kb = total_ukuran(struktur)
print(f'Total ukuran_kb skripsi: {ukuran_kb} KB')

'''
Tugas B — Hitung Jumlah File
Kamu penasaran, ada berapa file di seluruh folder skripsimu?
'''
def hitung_file(folder: dict) -> int:
    jumlah = 0
    for file in folder.values():
        if type(file) == dict:
            jumlah += hitung_file(file)
        else:
            jumlah += 1
    
    return jumlah

banyak_file = hitung_file(struktur)
print(f'Jumlah file: {banyak_file} file')

'''
Tugas C — Cari File Terbesar (30 poin)
Kamu curiga ada satu file yang ukurannya sangat besar dan memakan storage.
Buat fungsi yang mencari nama_file file dengan ukuran_kb terbesar beserta
ukurannya.
'''
def cari_terbesar(folder: dict) -> tuple:
# Kembalikan (nama_file, ukuran_kb)
    nama_file = ''
    ukuran_kb = 0

    for key, value in folder.items():
        if type(value) == dict: # kalau folder
            nama_dalam, ukuran_dalam = cari_terbesar(value)

            if ukuran_dalam > ukuran_kb:
                ukuran_kb = ukuran_dalam
                nama_file = nama_dalam
        else:
            if value > ukuran_kb:
                ukuran_kb = value
                nama_file = key
            
    return nama_file, ukuran_kb

nama, ukuran = cari_terbesar(struktur)
print(f'File terbesar: {nama}, {ukuran} KB')
print()

'''
Tugas D — Cetak Struktur Folder
Kamu ingin mencetak seluruh isi folder seperti tampilan tree di terminal —
dengan indentasi yang menunjukkan kedalaman setiap item.
'''
def tampilkan_tree(folder: dict, nama: str = "root", level: int = 0):
        indentasi = ' ' * level
        print(f'{indentasi} |{nama}|')

        for key, value in folder.items():
            if type(value) == dict:
                tampilkan_tree(value, key, level + 1)
            else:
                print(f'{indentasi} # {key} ({value} KB)') 

tampilkan_tree(struktur)