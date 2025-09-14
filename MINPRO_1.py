# MINI_PROJECT_1 - "SISTEM REMINDER TUGAS"
# Nama : Vidya Khansa Mizan
# NIM : 2509116052
# Kelas/Mata kuliah : B/Praktikum Dasar-Dasar Pemrograman

# MENU UTAMA
print("-"*35)
print("~~ MENU PILIHAN 'REMINDER TUGAS' ~~")
print("1. List Lengkap Tugas di Bulan Ini")
print("2. Cek Tugas+Deadline Per-Matkul")
print("3. Tambah Tugas")
print("4. Exit")
print("-"*35)

# PERTANYAAN UNTUK MASUK KE STEP SELANJUTNYA
tanyaa = int(input("Ketik nomor menu yang dituju (1-4): ")) 

# LIST TUGAS BESERTA DEADLINE DI BULAN INI
tugas_deadline = [
    ["Ringkasan Agama 6 Pertemuan", "18 September 2025"],
    ["Study Case 2", "12 September 2025"],
    ["MinPro 1 Praktikum DDP", "14 September 2025"],
    ["Tugas Pendidikan Pancasila", "17 September 2025"],
    ["Diagram Fishbone", "17 September 2025"],
    ["MinPro 1 Praktikum PTI", "20 September 2025"]
]

# KONDISI PERTAMA (READ)
if tanyaa == 1:
    print("\nbaikk, berikut ini adalah list tugas kamu di bulan ini: ")
    list_tugas = (
        f"- {tugas_deadline[0][0]} dengan deadline di tanggal {tugas_deadline[0][1]}\n"
        f"- {tugas_deadline[1][0]} dengan deadline di tanggal {tugas_deadline[1][1]}\n"
        f"- {tugas_deadline[2][0]} dengan deadline di tanggal {tugas_deadline[2][1]}\n"
        f"- {tugas_deadline[3][0]} dengan deadline di tanggal {tugas_deadline[3][1]}\n"
        f"- {tugas_deadline[4][0]} dengan deadline di tanggal {tugas_deadline[4][1]}\n"
        f"- {tugas_deadline[5][0]} dengan deadline di tanggal {tugas_deadline[5][1]}\n"
    )
    print(list_tugas)
    print("banyak jugaa yaa, yukk nyicil dari sekarang (˵•̀ ᴗ-˵)✧")


# KONDISI KEDUA
elif tanyaa == 2:
    tasks = (input("\nMasukkan Mata kuliah yang ingin dicari? "))
    if tasks == "Agama":
        print(f"ADAA! tugasnya {tugas_deadline[0][0]}, dan deadlinenya di tanggal {tugas_deadline[0][1]}, SEMANGATT!!")
    elif tasks == "Praktikum DDP":
        print(f"ADAA! tugasnya {tugas_deadline[1][0]}, dan deadlinenya di tanggal {tugas_deadline[1][1]}. Terus ada satu lagi, {tugas_deadline[2][0]} dengan deadline di tanggal {tugas_deadline[2][1]}, SEMANGATT!!")
    elif tasks == "PKN":
        print(f"ADAA! tugasnya {tugas_deadline[3][0]}, dan deadlinenya di tanggal {tugas_deadline[3][1]}, SEMANGATT!!")
    elif tasks == "KSI":
        print(f"ADAA! tugasnya {tugas_deadline[4][0]}, dan deadlinenya di tanggal {tugas_deadline[4][1]}, SEMANGATT!!")
    elif tasks == "Praktikum PTI":
        print(f"ADAA! tugasnya {tugas_deadline[5][0]}, dan deadlinenya di tanggal {tugas_deadline[5][1]}, SEMANGATT!!")
    else:
        print("SELAMATT!! kamu tidak ada tugas:D")


# KONDISI KE-TIGA (CREATE)
elif tanyaa == 3:
    print("\nIsilah format di bawah ini!")
    nama = input("Nama tugas:  ")
    deadline = input("Deadline/Tenggat: ")

    neww_tasks = (nama, deadline)
    tugas_deadline.append(neww_tasks)
    print("Tugas sudah ditambahkann^^")

    print("\nBerikut list tugas terbaru kamuu:")
    list_tugas = (
        f"- {tugas_deadline[0][0]} dengan deadline di tanggal {tugas_deadline[0][1]}\n"
        f"- {tugas_deadline[1][0]} dengan deadline di tanggal {tugas_deadline[1][1]}\n"
        f"- {tugas_deadline[2][0]} dengan deadline di tanggal {tugas_deadline[2][1]}\n"
        f"- {tugas_deadline[3][0]} dengan deadline di tanggal {tugas_deadline[3][1]}\n"
        f"- {tugas_deadline[4][0]} dengan deadline di tanggal {tugas_deadline[4][1]}\n"
        f"- {tugas_deadline[5][0]} dengan deadline di tanggal {tugas_deadline[5][1]}\n"
        f"- {tugas_deadline[6][0]} dengan deadline di tanggal {tugas_deadline[6][1]}\n"
    )
    print(list_tugas)
    print("SEMANGAATT NGERJAINNYAA!!")


# KONDISI KE-EMPAT
elif tanyaa == 4:
    print("\nokeeyy, sampai jumpaa nanti yaa (づ๑•ᴗ•๑)づ♡")


# KONDISI APABILA TIDAK MEMENUHI KETENTUAN DI SOAL
else:
    print("\nmohon maaf nomor yang anda masukkan tidak valid (╥﹏╥;)")