# 🔁 Octra Auto Runner (Single Wallet)

Script Python ini digunakan untuk melakukan **transaksi otomatis di jaringan Octra** dari satu wallet.  
Script ini menjalankan serangkaian operasi termasuk:

- Multi-Send ke banyak penerima
- Enkripsi saldo
- Dekripsi saldo
- Private transfer
- Klaim private transfer

Semua proses disertai **retry otomatis dan delay yang aman** untuk memastikan setiap transaksi berhasil diproses node.

---

## ⚙️ Fitur Utama

| Proses             | Deskripsi                                                                 |
|--------------------|---------------------------------------------------------------------------|
| 🔁 Multi-Send       | Mengirim OCT ke banyak penerima dari file `p.txt` (delay 15 detik/tx)     |
| 🔐 Enkripsi         | Enkripsi saldo sebesar 5 OCT (retry hingga sukses, delay 20 detik)        |
| 🔓 Dekripsi         | Dekripsi saldo sebesar 1 OCT (delay 1 menit saat gagal, 20 detik sesudah) |
| 🕵️ Private Transfer | Kirim privat 0.1 OCT ke setiap penerima (delay 60 detik antar tx)         |
| 📥 Klaim Transfer   | Klaim semua private transfer yang masuk (retry per ID jika gagal)         |

---

## 📂 Struktur File

```text
project-folder/
├── auto_runner.py     # Script utama ini
├── cli.py             # Modul CLI untuk transaksi (harus terhubung dengan node Octra)
└── p.txt              # Daftar penerima dan jumlah OCT
└── wallet.json        # Privatekey wallet octra
```
## ✍️ Format File `p.txt`
Setiap baris berisi:
<octra_address> <jumlah_OCT>
### Contoh:
oct8rjAyUM93vQ5VXBdbfEtAUsFQxM75kac7kpgjVSu1WAg 0.5  
oct9Yjx6Sks5Z8bKqVzGChsN6CkWqz5mB59EAFLSnpDFoKd 1.25
## ✍️ Format File `wallet.json`
itu sama aja kek kita mau run client Octra jadi ubah terlbih dahulu

## ▶️ Cara Menjalankan

### Pastikan environment aktif:
```bash
python3 -m venv venv
source venv/bin/activate
```
## Clone repositori:
```bash
git clone https://github.com/kenjisubagja/octraV2
cd octraV2
```
```bash
pip install -r requirements.txt
```
Run
```bash
python3 auto_runner.py
```
## 📌 Ketahanan & Retry
Jika ada transaksi gagal (misal: nonce conflict, tidak ada public key, node lambat), script akan:

Menunggu beberapa detik

Mencoba ulang (hingga berhasil)

Tidak lanjut ke langkah berikutnya sebelum langkah sebelumnya sukses
## 👤
Created By Kenjisubagja:
**Contact me**  
📨 Telegram: [@kenjisubagja](https://t.me/kenjisubagja)  
🐦 Twitter/X: [@kenjisubagja](https://x.com/kenjisubagja)
