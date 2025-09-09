# kasir.py
import tkinter as tk
from tkinter import messagebox
import os, csv, datetime

DATA_DIR = "data"
TRANSAKSI_FILE = os.path.join(DATA_DIR, "transaksi.csv")
SESSION_FILE = os.path.join(DATA_DIR, "session.txt")

MENU_DEFAULT = {
    "Nasi Goreng": 12000,
    "Mie Goreng": 10000,
    "Ayam Geprek": 15000,
    "Es Teh": 4000,
    "Es Jeruk": 6000,
    "Air Mineral": 3000,
}

def ensure_files():
    os.makedirs(DATA_DIR, exist_ok=True)
    if not os.path.exists(TRANSAKSI_FILE):
        with open(TRANSAKSI_FILE, "w", encoding="utf-8", newline="") as f:
            w = csv.writer(f)
            w.writerow(["tanggal","waktu","item","harga","jumlah","total","kasir"])

def get_session_user():
    if not os.path.exists(SESSION_FILE):
        return None
    with open(SESSION_FILE, "r", encoding="utf-8") as f:
        return f.read().strip() or None

def on_item_change(*_):
    item = var_item.get()
    if item in MENU_DEFAULT:
        ent_harga.delete(0, tk.END)
        ent_harga.insert(0, str(MENU_DEFAULT[item]))

def simpan_transaksi():
    item = var_item.get().strip()
    harga_txt = ent_harga.get().strip()
    jumlah_txt = ent_jumlah.get().strip()

    if not item or not harga_txt or not jumlah_txt:
        messagebox.showerror("Error", "Semua kolom wajib diisi.")
        return
    try:
        harga = int(harga_txt)
        jumlah = int(jumlah_txt)
        if harga < 0 or jumlah <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Harga/jumlah harus angka yang benar.")
        return

    total = harga * jumlah
    now = datetime.datetime.now()
    row = [now.date().isoformat(), now.strftime("%H:%M:%S"), item, harga, jumlah, total, USER]

    with open(TRANSAKSI_FILE, "a", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(row)

    messagebox.showinfo("Sukses", f"Disimpan: {item} x {jumlah} = Rp{total}")
    ent_jumlah.delete(0, tk.END)

def ringkas_hari_ini():
    if not os.path.exists(TRANSAKSI_FILE):
        messagebox.showinfo("Ringkasan", "Belum ada transaksi.")
        return
    today = datetime.date.today().isoformat()
    total_hari_ini = 0
    with open(TRANSAKSI_FILE, "r", encoding="utf-8") as f:
        r = csv.DictReader(f)
        for row in r:
            if row["tanggal"] == today:
                total_hari_ini += int(row["total"])
    messagebox.showinfo("Pendapatan Hari Ini", f"Total: Rp{total_hari_ini}")

# === Start ===
ensure_files()
USER = get_session_user()
if not USER:
    # tidak ada sesi → minta login dulu
    from tkinter import Tk
    root = Tk()
    root.withdraw()
    messagebox.showerror("Sesi Habis", "Silakan login dulu lewat login.py")
    root.destroy()
    raise SystemExit

root = tk.Tk()
root.title(f"Kasir Kantin - Login sebagai {USER}")

frm = tk.Frame(root, padx=16, pady=16)
frm.pack()

# Pilihan item
tk.Label(frm, text="Pilih Menu").grid(row=0, column=0, sticky="w")
var_item = tk.StringVar(value=list(MENU_DEFAULT.keys())[0])
opt = tk.OptionMenu(frm, var_item, *MENU_DEFAULT.keys(), command=lambda *_: on_item_change())
opt.grid(row=0, column=1, sticky="we", pady=4)

# Harga (bisa disesuaikan)
tk.Label(frm, text="Harga (Rp)").grid(row=1, column=0, sticky="w")
ent_harga = tk.Entry(frm, width=20)
ent_harga.grid(row=1, column=1, sticky="we", pady=4)

# Jumlah
tk.Label(frm, text="Jumlah").grid(row=2, column=0, sticky="w")
ent_jumlah = tk.Entry(frm, width=20)
ent_jumlah.grid(row=2, column=1, sticky="we", pady=4)

# set harga awal sesuai item default
on_item_change()

# Tombol
btn_save = tk.Button(frm, text="Simpan Transaksi", command=simpan_transaksi, width=20)
btn_save.grid(row=3, column=0, columnspan=2, pady=(8,2))

btn_sum = tk.Button(frm, text="Pendapatan Hari Ini", command=ringkas_hari_ini, width=20)
btn_sum.grid(row=4, column=0, columnspan=2, pady=2)

root.mainloop()
