
import sqlite3

# Membuat database
conn = sqlite3.connect("database_siswa.db")
cursor = conn.cursor()

# Membuat tabel siswa
cursor.execute("""
CREATE TABLE IF NOT EXISTS siswa (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nama TEXT NOT NULL,
    kelas TEXT NOT NULL,
    jurusan TEXT NOT NULL,
    tanggal_lahir TEXT NOT NULL
)
""")
conn.commit()


def input_data():
    print("\n=== INPUT DATA SISWA ===")

    nama = input("Nama siswa       : ")
    kelas = input("Kelas            : ")
    jurusan = input("Jurusan          : ")
    tanggal_lahir = input("Tanggal lahir (DD-MM-YYYY): ")

    cursor.execute("""
        INSERT INTO siswa (nama, kelas, jurusan, tanggal_lahir)
        VALUES (?, ?, ?, ?)
    """, (nama, kelas, jurusan, tanggal_lahir))

    conn.commit()
    print("\nData siswa berhasil disimpan!")


def tampilkan_data():
    print("\n=== DATA SISWA SMA ===")

    cursor.execute("SELECT * FROM siswa")
    data = cursor.fetchall()

    if not data:
        print("Belum ada data siswa.")
    else:
        for siswa in data:
            print("-" * 35)
            print(f"ID            : {siswa[0]}")
            print(f"Nama          : {siswa[1]}")
            print(f"Kelas         : {siswa[2]}")
            print(f"Jurusan       : {siswa[3]}")
            print(f"Tanggal lahir : {siswa[4]}")

        print("-" * 35)


# Menu utama
while True:
    print("\n==========================")
    print("   DATABASE SISWA SMA")
    print("==========================")
    print("1. Input Data")
    print("2. Tampilkan Data")
    print("3. Keluar")

    pilihan = input("Pilih menu (1-3): ")

    if pilihan == "1":
        input_data()
    elif pilihan == "2":
        tampilkan_data()
    elif pilihan == "3":
        print("Program selesai. Terima kasih!")
        break
    else:
        print("Pilihan tidak valid, silakan coba lagi.")

conn.close()
