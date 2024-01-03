import tkinter as tk
from tkinter import messagebox

# Inisialisasi perpustakaan sebagai list kosong
perpustakaan = []

# Fungsi untuk menambahkan buku ke perpustakaan
def tambah_buku():
    judul = entry_judul.get()
    penulis = entry_penulis.get()
    
    if judul and penulis:
        buku_baru = {'judul': judul, 'penulis': penulis}
        perpustakaan.append(buku_baru)
        messagebox.showinfo("Info", f"Buku '{judul}' oleh {penulis} berhasil ditambahkan.")
    else:
        messagebox.showwarning("Peringatan", "Masukkan judul dan penulis buku.")

# Fungsi untuk menampilkan daftar buku di perpustakaan
def tampilkan_perpustakaan():
    if not perpustakaan:
        messagebox.showinfo("Info", "Perpustakaan kosong. Tambahkan buku terlebih dahulu.")
    else:
        daftar_buku = "\n".join([f"{buku['judul']} oleh {buku['penulis']}" for buku in perpustakaan])
        messagebox.showinfo("Daftar Buku", f"Daftar Buku di Perpustakaan:\n{daftar_buku}")

# Membuat GUI menggunakan Tkinter
root = tk.Tk()
root.title("Aplikasi Perpustakaan")

label_judul = tk.Label(root, text="Judul Buku:")
label_judul.pack()

entry_judul = tk.Entry(root)
entry_judul.pack()

label_penulis = tk.Label(root, text="Penulis Buku:")
label_penulis.pack()

entry_penulis = tk.Entry(root)
entry_penulis.pack()

tambah_button = tk.Button(root, text="Tambah Buku", command=tambah_buku)
tambah_button.pack()

tampilkan_button = tk.Button(root, text="Tampilkan Perpustakaan", command=tampilkan_perpustakaan)
tampilkan_button.pack()

keluar_button = tk.Button(root, text="Keluar", command=root.destroy)
keluar_button.pack()

root.mainloop()
