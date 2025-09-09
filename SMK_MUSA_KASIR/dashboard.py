import tkinter as tk
from tkinter import ttk, messagebox
import csv, os

os.makedirs("data", exist_ok=True)
file_path = "data/transaksi.csv"

# kalau belum ada file, buat header
if not os.path.exists(file_path):
    with open(file_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "item", "harga", "jumlah", "total"])

def load_data():
    for row in tree.get_children():
        tree.delete(row)
    with open(file_path, "r") as f:
        reader = csv.reader(f)
        next(reader)  # skip header
        for row in reader:
            if row:
                tree.insert("", "end", values=row)

def tambah_data():
    item = entry_item.get()
    harga = entry_harga.get()
    jumlah = entry_jumlah.get()

    if not item or not harga or not jumlah:
        messagebox.showwarning("Peringatan", "Semua field harus diisi!")
        return

    try:
        harga = int(harga)
        jumlah = int(jumlah)
    except:
        messagebox.showerror("Error", "Harga dan Jumlah harus angka!")
        return

    total = harga * jumlah
    # hitung id baru
    with open(file_path, "r") as f:
        reader = list(csv.reader(f))
        next(reader)  
        new_id = len(reader) + 1

    with open(file_path, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([new_id, item, harga, jumlah, total])

    entry_item.delete(0, tk.END)
    entry_harga.delete(0, tk.END)
    entry_jumlah.delete(0, tk.END)
    load_data()

def hapus_data():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Peringatan", "Pilih data dulu!")
        return

    item_id = tree.item(selected)["values"][0]

    with open(file_path, "r") as f:
        rows = list(csv.reader(f))
    header, data = rows[0], rows[1:]

    data = [row for row in data if row[0] != str(item_id)]

    with open(file_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(data)

    load_data()

root = tk.Tk()
root.title("Dashboard Kasir Kantin SMK MUSA")

# Form input
tk.Label(root, text="Item").grid(row=0, column=0)
entry_item = tk.Entry(root)
entry_item.grid(row=0, column=1)

tk.Label(root, text="Harga").grid(row=1, column=0)
entry_harga = tk.Entry(root)
entry_harga.grid(row=1, column=1)

tk.Label(root, text="Jumlah").grid(row=2, column=0)
entry_jumlah = tk.Entry(root)
entry_jumlah.grid(row=2, column=1)

tk.Button(root, text="Tambah", command=tambah_data).grid(row=3, column=0)
tk.Button(root, text="Hapus", command=hapus_data).grid(row=3, column=1)

# Tabel
columns = ("id", "item", "harga", "jumlah", "total")
tree = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
tree.grid(row=4, column=0, columnspan=2)

load_data()

root.mainloop()
