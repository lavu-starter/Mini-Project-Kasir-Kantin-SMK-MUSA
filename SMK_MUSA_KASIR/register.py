import tkinter as tk
from tkinter import messagebox
import csv, os

os.makedirs("data", exist_ok=True)

def register_user():
    username = entry_user.get()
    password = entry_pass.get()

    if not username or not password:
        messagebox.showwarning("Peringatan", "Semua field harus diisi!")
        return

    with open("data/users.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([username, password])

    messagebox.showinfo("Sukses", "Akun berhasil dibuat!")
    entry_user.delete(0, tk.END)
    entry_pass.delete(0, tk.END)

root = tk.Tk()
root.title("Register")

tk.Label(root, text="Username").pack()
entry_user = tk.Entry(root)
entry_user.pack()

tk.Label(root, text="Password").pack()
entry_pass = tk.Entry(root, show="*")
entry_pass.pack()

tk.Button(root, text="Daftar", command=register_user).pack()

root.mainloop()
