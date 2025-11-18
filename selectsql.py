import sqlite3

# Buka koneksi ke database yang sudah dibuat
conn = sqlite3.connect('universitas.db')
cursor = conn.cursor()

print("="*50)
print("1. DATA STRUCTURE (Struktur Tabel)")
print("="*50)

# Perintah SQL untuk melihat info kolom tabel (PRAGMA)
cursor.execute("PRAGMA table_info(nilai_siswa)")
struktur = cursor.fetchall()

print(f"{'ID':<5} {'Nama Kolom':<20} {'Tipe Data':<10}")
print("-" * 40)
for kolom in struktur:
    # kolom[0] = cid, kolom[1] = nama, kolom[2] = tipe
    print(f"{kolom[0]:<5} {kolom[1]:<20} {kolom[2]:<10}")


print("\n" + "="*50)
print("2. ISI DATA (SELECT * FROM nilai_siswa)")
print("="*50)

# Perintah SQL untuk melihat isi data
cursor.execute("SELECT * FROM nilai_siswa")
data_siswa = cursor.fetchall()

if not data_siswa:
    print("Tabel masih kosong.")
else:
    # Header sederhana
    print(f"{'ID':<5} {'Nama':<20} {'Bio':<5} {'Fis':<5} {'Ing':<5} {'Prediksi':<15}")
    print("-" * 60)
    for baris in data_siswa:
        print(f"{baris[0]:<5} {baris[1]:<20} {baris[2]:<5} {baris[3]:<5} {baris[4]:<5} {baris[5]:<15}")

conn.close()