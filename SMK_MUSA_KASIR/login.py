import tkinter as tk
from tkinter import messagebox
import csv, subprocess, os

def cek_login():
    username = entry_user.get()
    password = entry_pass.get()

    if not os.path.exists("data/users.csv"):
        messagebox.showerror("Error", "Belum ada user terdaftar!")
        return

    with open("data/users.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row and row[0] == username and row[1] == password:
                messagebox.showinfo("Login", "Login berhasil!")
                root.destroy()
                subprocess.Popen(["python", "dashboard.py"])
                return
    messagebox.showerror("Login", "Username atau password salah!")

root = tk.Tk()
root.title("Login")

tk.Label(root, text="Username").pack()
entry_user = tk.Entry(root)
entry_user.pack()

tk.Label(root, text="Password").pack()
entry_pass = tk.Entry(root, show="*")
entry_pass.pack()

tk.Button(root, text="Login", command=cek_login).pack()

root.mainloop()
