# Mini Project Kasir Kantin SMK MUSA

## Deskripsi
Proyek ini adalah aplikasi kasir sederhana untuk **SMK MUSA**, dibuat menggunakan **Python GUI (Tkinter)** dan **CSV** sebagai penyimpanan data. 
Siswa kelas X dapat belajar konsep **CRUD (Create, Read, Update, Delete)** sambil mempraktikkan pemrograman Python secara langsung.

Aplikasi ini terdiri dari tiga modul utama:
1. **register.py** → untuk mendaftar akun user baru.
2. **login.py** → untuk login user dan membuka dashboard.
3. **dashboard.py** → halaman utama untuk manajemen transaksi kasir kantin.

Semua data tersimpan di folder `data/`:
- `users.csv` → menyimpan username dan password.
- `transaksi.csv` → menyimpan data transaksi kasir (id, item, harga, jumlah, total).

## Fitur
- Register akun baru
- Login user
- Tambah transaksi baru (Create)
- Lihat daftar transaksi (Read)
- Hapus transaksi (Delete)
- CRUD sederhana menggunakan CSV
- Tabel transaksi menggunakan Tkinter Treeview

## Cara Menjalankan
1. Clone repository atau download ZIP.
2. Pastikan Python 3.x sudah terinstal.
3. Jalankan `register.py` untuk membuat akun baru.
4. Jalankan `login.py` untuk login.
5. Setelah login berhasil, `dashboard.py` akan terbuka otomatis.
6. Lakukan manajemen transaksi kasir di dashboard.

## Struktur Folder
SMK_MUSA_KASIR/
│── register.py
│── login.py
│── dashboard.py
└── data/
├── users.csv
└── transaksi.csv


## Catatan
- Proyek ini dibuat untuk keperluan **praktik kelas X SMK**.
- Data disimpan dalam format CSV untuk mempermudah pemahaman CRUD.
