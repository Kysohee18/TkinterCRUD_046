import tkinter as tk
from tkinter import messagebox
import sqlite3

#konfigurasi database

def setup_database():
    """Membuat database dan table 'nilai_siswa' jika belum ada."""
    try:
        conn = sqlite3.connect('universitas.db')
        cursor = conn.cursor()

        # Buat table nilai_siswa
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS nilai_siswa (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama_siswa TEXT NOT NULL,
            biologi INTEGER,
            fisika INTEGER,
            inggris INTEGER,
            prediksi_fakultas TEXT
        )
        ''')
        
        conn.commit()
        
    except sqlite3.Error as e:
        messagebox.showerror("Database Error", f"Gagal setup database: {e}")
        
    finally:
        if conn:
            conn.close()

#logika penentuan

def submit_data():
    """Dipanggil saat tombol 'Submit Nilai' ditekan."""
    
    nama = entry_nama.get()
    
    if not nama or not entry_bio.get() or not entry_fis.get() or not entry_ing.get():
        messagebox.showwarning("Input Kosong", "Semua field harus diisi!")
        return

    try:
        bio = int(entry_bio.get())
        fis = int(entry_fis.get())
        ing = int(entry_ing.get())
    except ValueError:
        messagebox.showerror("Input Salah", "Nilai Biologi, Fisika, dan Inggris harus angka!")
        return

    # Logika Penentuan Prediksi Fakultas
    prediksi = ""
    if bio >= fis and bio >= ing:
        prediksi = "Kedokteran"
    elif fis >= bio and fis >= ing:
        prediksi = "Teknik"
    elif ing >= bio and ing >= fis:
        prediksi = "Bahasa"
    else:
        prediksi = "Belum Terdeteksi"

    # Simpan data ke Database SQLite
    try:
        conn = sqlite3.connect('universitas.db')
        cursor = conn.cursor()
        
        cursor.execute('''
        INSERT INTO nilai_siswa (nama_siswa, biologi, fisika, inggris, prediksi_fakultas)
        VALUES (?, ?, ?, ?, ?)
        ''', (nama, bio, fis, ing, prediksi))
        
        conn.commit()
        
        messagebox.showinfo("Sukses", f"Data {nama} berhasil disimpan!\nPrediksi Fakultas: {prediksi}")
        
        clear_entries()

    except sqlite3.Error as e:
        messagebox.showerror("Database Error", f"Gagal menyimpan data: {e}")
    
    finally:
        if conn:
            conn.close()

def clear_entries():
    """Membersihkan semua entry fields."""
    entry_nama.delete(0, tk.END)
    entry_bio.delete(0, tk.END)
    entry_fis.delete(0, tk.END)
    entry_ing.delete(0, tk.END)
    entry_nama.focus()

# GUI menggunakan Tkinter

# Inisialisasi window utama
root = tk.Tk()
root.title("Aplikasi Prediksi Fakultas")
root.geometry("400x250")
root.resizable(False, False)

main_frame = tk.Frame(root, padx=20, pady=20)
main_frame.pack(expand=True)

#Buat Widgets (Label dan Entry) 
tk.Label(main_frame, text="Nama Siswa:").grid(row=0, column=0, sticky="w", pady=5)
entry_nama = tk.Entry(main_frame, width=30)
entry_nama.grid(row=0, column=1, pady=5)

tk.Label(main_frame, text="Nilai Biologi:").grid(row=1, column=0, sticky="w", pady=5)
entry_bio = tk.Entry(main_frame, width=30)
entry_bio.grid(row=1, column=1, pady=5)

tk.Label(main_frame, text="Nilai Fisika:").grid(row=2, column=0, sticky="w", pady=5)
entry_fis = tk.Entry(main_frame, width=30)
entry_fis.grid(row=2, column=1, pady=5)

tk.Label(main_frame, text="Nilai Inggris:").grid(row=3, column=0, sticky="w", pady=5)
entry_ing = tk.Entry(main_frame, width=30)
entry_ing.grid(row=3, column=1, pady=5)

#  Buat Button Submit 
submit_button = tk.Button(
    main_frame, 
    text="Submit Nilai", 
    command=submit_data, # Panggil fungsi submit_data
    font=('Arial', 10, 'bold'),
    bg='#AED6F1',
    padx=10
)
submit_button.grid(row=4, columnspan=2, pady=20)

#memanggil program

if __name__ == "__main__":
    # Setup database saat program pertama kali jalan
    setup_database()
    
    # Jalankan aplikasi GUI
    root.mainloop()