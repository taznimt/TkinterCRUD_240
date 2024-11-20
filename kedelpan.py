import sqlite3  # Mengimpor modul sqlite3 untuk berinteraksi dengan database SQLite
from tkinter import Tk, Label, Entry, Button, StringVar, messagebox, ttk # Mengimpor komponen dari modul tkinter untuk membuat GU

# Fungsi untuk membuat database dan tabel
def create_database():
    conn = sqlite3.connect('nilai_siswa.db')  # Membuat koneksi ke database SQLite
    cursor = conn.cursor()  # Membuat objek cursor untuk mengeksekusi perintah SQL
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS nilai_siswa (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            nama_siswa TEXT,
            biologi INTEGER,
            fisika INTEGER,
            inggris INTEGER,
            prediksi_fakultas TEXT
        )
    ''')  # Membuat tabel jika belum ada
    conn.commit() # Menyimpan perubahan ke database
    conn.close() # Menutup koneksi ke database
    
def fetch_data():
        conn = sqlite3.connect('nilai_siswa.db') # Membuka koneksi ke database
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM nilai_siswa") # Mengambil semua data dari tabel
        rows = cursor.fetchall()  # Mengambil semua hasil query
        conn.close() # Menutup koneksi
        return rows  # Mengembalikan hasil
def save_to_database(nama, biologi, fisika, inggris, prediksi):
      conn = sqlite3.connect('nilai_siswa.db') # Membuka koneksi ke database
      cursor = conn.cursor()
      cursor = conn.cursor()
      cursor.execute('''
                     INSERT INTO nilai_siswa (nama_siswa, biologi, fisika, inggris, prediksi_fakultas)
                     VALUES (?, ?, ?, ?)
                     ''', (nama, biologi, fisika, inggris, prediksi)) # Menyimpan data siswa baru ke dalam tabel
      conn.commit() # Menyimpan perubahan
      conn.close() # Menutup koneksi

def update_database(record_id, nama, biologi, fisika, inggris, prediksi):
      conn = sqlite3.connect('nilai_siswa.db') # Membuka koneksi ke database
      cursor = conn.cursor()
      cursor.execute('''
                     UPDATE nilai_siswa
                     SET nama_siswa = ?, fisika =?, inggris = ?, prediksi_fakultas = ?
                     WHERE id + ?
    ''', (nama, biologi, fisika, inggris, prediksi, record_id))
      conn.commit() # Menyimpan perubahan
      conn.close()  # Menutup koneksi

def calculate_prediction(biologi, fisika, inggris):   # Fungsi untuk menghitung prediksi fakultas berdasarkan nilai
      if biologi > fisika and biologi > inggris:
            return "Kedokteran" # Jika nilai biologi tertinggi
      elif fisika > biologi and fisika > inggris:
            return "Teknik" # Jika nilai fisika tertinggi
      elif inggris > biologi and inggris > fisika:
            return "Bahasa"  # Jika nilai inggris tertinggi
      else:
            return "Tidak Dikatehui"  # Jika tidak ada nilai tertinggi yang jelas
      
import sqlite3 # Mengimpor modul sqlite3 untuk berinteraksi dengan database SQLite.
from tkinter import Tk, Label, Entry, Button, StringVar, messagebox, ttk  # Mengimpor komponen dari modul tkinter untuk membuat antarmuka pengguna grafis (GUI).

# Fungsi untuk membuat database dan tabel
def create_database():
    conn = sqlite3.connect('nilai_siswa.db')   # Membuat koneksi ke database SQLite dengan nama 
    cursor = conn.cursor()  # Membuat objek cursor untuk mengeksekusi perintah SQL.
    # Menjalankan perintah SQL untuk membuat tabel 'nilai_siswa' jika tabel tersebut belum ada.
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS nilai_siswa (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama_siswa TEXT,
            biologi INTEGER,
            fisika INTEGER,
            inggris INTEGER,
            prediksi_fakultas TEXT
        )
    ''')
    conn.commit() # Menyimpan perubahan yang telah dilakukan ke database.
    conn.close()  # Menutup koneksi ke database untuk membebaskan sumber daya.

def fetch_data():
    conn = sqlite3.connect('nilai_siswa.db')  # Membuka koneksi ke database SQLite dengan nama 
    cursor = conn.cursor()   # Membuat objek cursor untuk mengeksekusi perintah SQL.
    cursor.execute("SELECT * FROM nilai_siswa")  # Menjalankan perintah SQL untuk mengambil semua data dari tabel 'nilai_siswa'.
    rows = cursor.fetchall() # Mengambil semua hasil query dan menyimpannya dalam variabel 'rows'.
    conn.close() # Menutup koneksi ke database.
    return rows # Mengembalikan hasil query (semua data siswa) ke pemanggil fungsi.

def save_to_database(nama, biologi, fisika, inggris, prediksi):
    conn = sqlite3.connect('nilai_siswa.db')  # Membuka koneksi ke database SQLite dengan nama 'nilai_siswa.db'.
    cursor = conn.cursor()  # Membuat objek cursor untuk mengeksekusi perintah SQL
    # Menjalankan perintah SQL untuk menyimpan data siswa baru ke dalam tabel 'nilai_siswa'.
    cursor.execute('''
        INSERT INTO nilai_siswa (nama_siswa, biologi, fisika, inggris, prediksi_fakultas)
        VALUES (?, ?, ?, ?, ?)
    ''', (nama, biologi, fisika, inggris, prediksi)) # Menggunakan parameter untuk mencegah SQL injection.
    conn.commit() # Menyimpan perubahan yang telah dilakukan ke database.
    conn.close() # Menutup koneksi ke database.

def update_database(record_id, nama, biologi, fisika, inggris, prediksi):
    conn = sqlite3.connect('nilai_siswa.db')  # Membuka koneksi ke database SQLite dengan nama 'nilai_siswa.db'.
    cursor = conn.cursor()  # Membuat objek cursor untuk mengeksekusi perintah SQL.
    # Menjalankan perintah SQL untuk memperbarui data siswa berdasarkan ID yang diberikan.
    cursor.execute('''
        UPDATE nilai_siswa
        SET nama_siswa = ?, biologi = ?, fisika = ?, inggris = ?, prediksi_fakultas = ?
        WHERE id = ?
    ''', (nama, biologi, fisika, inggris, prediksi, record_id)) # Menggunakan parameter untuk mencegah SQL injection.
    conn.commit()  # Menyimpan perubahan yang telah dilakukan ke database.
    conn.close()  # Menutup koneksi ke database.

def delete_database(record_id):
    conn = sqlite3.connect('nilai_siswa.db')   # Membuka koneksi ke database SQLite dengan nama 'nilai_siswa.db'.
    cursor = conn.cursor()  # Membuat objek cursor untuk mengeksekusi perintah SQL.
      # Menjalankan perintah SQL untuk menghapus data siswa berdasarkan ID yang diberikan.
    cursor.execute('DELETE FROM nilai_siswa WHERE id = ?', (record_id,)) 
    conn.commit() # Menyimpan perubahan yang telah dilakukan ke database.
    conn.close() # Menutup koneksi ke database.

def calculate_prediction(biologi, fisika, inggris):
      # Fungsi untuk menghitung prediksi fakultas berdasarkan nilai yang diberikan.
    if biologi > fisika and biologi > inggris:
        return "Kedokteran"  # Jika nilai biologi tertinggi, kembalikan "Kedokteran".
    elif fisika > biologi and fisika > inggris:
        return "Teknik" # Jika nilai fisika tertinggi, kembalikan "Teknik".
    elif inggris > biologi and inggris > fisika:
        return "Bahasa" # Jika nilai inggris tertinggi, kembalikan "Bahasa".
    else:
        return "Tidak Diketahui" # Jika tidak ada nilai tertinggi yang jelas, kembalikan "Tidak Diketahui".

def submit():
    try:
        nama = nama_var.get() # Mengambil nama siswa dari variabel StringVar
        biologi = int(biologi_var.get())  # Mengambil nilai biologi dan mengonversinya ke integer
        fisika = int(fisika_var.get())  # Mengambil nilai fisika dan mengonversinya ke integer
        inggris = int(inggris_var.get()) # Mengambil nilai inggris dan mengonversinya ke integer

        if not nama:         # Memeriksa apakah nama siswa tidak kosong
            raise Exception("Nama siswa tidak boleh kosong.")
         # Menghitung prediksi fakultas berdasarkan nilai yang diberikan
        prediksi = calculate_prediction(biologi, fisika, inggris) 
         # Menyimpan data siswa ke database
        save_to_database(nama, biologi, fisika, inggris, prediksi)


        # Menampilkan pesan sukses kepada pengguna
        messagebox.showinfo("Sukses", f"Data berhasil disimpan!\nPrediksi Fakultas: {prediksi}")
        clear_inputs() # Menghapus input setelah penyimpanan
        populate_table()  # Memperbarui tabel untuk menampilkan data terbaru
    except ValueError as e:
        messagebox.showerror("Error", f"Input tidak valid: {e}")  # Menangani kesalahan konversi input ke integer

def update():
    try:
        if not selected_record_id.get(): # Memeriksa apakah ada ID record yang dipilih untuk diperbarui
            raise Exception("Pilih data dari tabel untuk di-update!") 

        record_id = int(selected_record_id.get())    # Mengambil ID record yang dipilih dan mengonversinya ke integer
        nama = nama_var.get() # Mengambil nama siswa dari variabel StringVar
        biologi = int(biologi_var.get()) # Mengambil nilai biologi dan mengonversinya ke integer
        fisika = int(fisika_var.get())  # Mengambil nilai fisika dan mengonversinya ke integer
        inggris = int(inggris_var.get()) # Mengambil nilai inggris dan mengonversinya ke integer

        if not nama:  # Memeriksa apakah nama siswa tidak kosong
            raise ValueError("Nama siswa tidak boleh kosong.")
        
        # Menghitung prediksi fakultas berdasarkan nilai yang diberikan
        prediksi = calculate_prediction(biologi, fisika, inggris) 
        # Memperbarui data siswa di database
        update_database(record_id, nama, biologi, fisika, inggris, prediksi)
         # Menampilkan pesan sukses kepada pengguna
        messagebox.showinfo("Sukses", "Data berhasil diperbarui!")
        clear_inputs()  # Menghapus input setelah pembaruan
        populate_table()  # Memperbarui tabel untuk menampilkan data terbaru
    except ValueError as e: # Menangani kesalahan konversi input ke integer atau kesalahan validasi lainnya
        messagebox.showerror("Error", f"Kesalahan: {e}") 

def delete():
    try:
        if not selected_record_id.get(): # Memeriksa apakah ada ID record yang dipilih untuk dihapus
            raise Exception("Pilih data dari tabel untuk dihapus!")

        record_id = int(selected_record_id.get())  # Mengambil ID record yang dipilih dan mengonversinya ke integer
        delete_database(record_id)   # Menghapus data dari database berdasarkan ID record
        messagebox.showinfo("Sukses", "Data berhasil dihapus!") # Menampilkan pesan sukses kepada pengguna
        clear_inputs()  # Menghapus input setelah penghapusan
        populate_table()  # Memperbarui tabel untuk menampilkan data terbaru
    except ValueError as e:
        messagebox.showerror("Error", f"Kesalahan: {e}")  # Menangani kesalahan konversi input ke integer

def clear_inputs():
     # Mengatur semua variabel input kembali ke string kosong
    nama_var.set("")
    biologi_var.set("")
    fisika_var.set("")
    inggris_var.set("")
    selected_record_id.set("") # Mengatur ID record yang dipilih kembali ke kosong


def populate_table():
     # Menghapus semua baris yang ada di tabel
    for row in tree.get_children():
        tree.delete(row)
     # Mengambil data terbaru dari database dan menambahkannya ke tabel
    for row in fetch_data():
        tree.insert('', 'end', values=row)

def fill_inputs_from_table(event):
    try:
        # Mengambil item yang dipilih dari tabel
        selected_item = tree.selection()[0] # Mengambil item pertama yang dipilih
        selected_row = tree.item(selected_item)['values']  # Mengambil nilai dari baris yang dipilih

        selected_record_id.set(selected_row[0])  # Mengisi ID record
        nama_var.set(selected_row[1]) # Mengisi nama siswa
        biologi_var.set(selected_row[2]) # Mengisi nilai biologi
        fisika_var.set(selected_row[3]) # Mengisi nilai fisika
        inggris_var.set(selected_row[4])  # Mengisi nilai inggris
    except IndexError:  # Menangani situasi di mana tidak ada item yang dipilih
        messagebox.showerror("Error", "Pilih data yang valid!")  

# Inisialisasi database
create_database()

# Membuat GUI dengan tkinter
root = Tk()
root.title("Prediksi Fakultas Siswa")

# Variabel tkinter
nama_var = StringVar()
biologi_var = StringVar()
fisika_var = StringVar()
inggris_var = StringVar()
selected_record_id = StringVar()  # Untuk menyimpan ID record yang dipilih
# Membuat label dan entry untuk Nama Siswa
Label(root, text="Nama Siswa").grid(row=0, column=0, padx=10, pady=5)
Entry(root, textvariable=nama_var).grid(row=0, column=1, padx=10, pady=5)
# Membuat label dan entry untuk Nilai Biologi
Label(root, text="Nilai Biologi").grid(row=1, column=0, padx=10, pady=5)
Entry(root, textvariable=biologi_var).grid(row=1, column=1, padx=10, pady=5)
# Membuat label dan entry untuk Nilai Fisika
Label(root, text="Nilai Fisika").grid(row=2, column=0, padx=10, pady=5)
Entry(root, textvariable=fisika_var).grid(row=2, column=1, padx=10, pady=5)
# Membuat label dan entry untuk Nilai Inggris
Label(root, text="Nilai Inggris").grid(row=3, column=0, padx=10, pady=5)
Entry(root, textvariable=inggris_var).grid(row=3, column=1, padx=10, pady=5)
# Membuat tombol untuk menambah, memperbarui, dan menghapus data
Button(root, text="Add", command=submit).grid(row=4, column=0, pady=10)
Button(root, text="Update", command=update).grid(row=4, column=1, pady=10)
Button(root, text="Delete", command=delete).grid(row=4, column=2, pady=10)

# Tabel untuk menampilkan data
columns = ("id", "nama_siswa", "biologi", "fisika", "inggris", "prediksi_fakultas")
tree = ttk.Treeview(root, columns=columns, show='headings')

# Mengatur posisi isi tabel di tengah
for col in columns:
    tree.heading(col, text=col.capitalize())
    tree.column(col, anchor='center') 

# Menempatkan treeview di grid
tree.grid(row=5, column=0, columnspan=3, padx=10, pady=10)
# Mengikat event klik pada treeview untuk mengisi input dari baris yang dipilih
tree.bind('<ButtonRelease-1>', fill_inputs_from_table)
# Memuat data awal ke dalam tabel
populate_table()
# Memulai loop utama aplikasi
root.mainloop()