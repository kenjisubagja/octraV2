# 🔄 Octra Auto Runner

Script Python untuk menjalankan transaksi **multi-wallet** otomatis di jaringan **Octra**, termasuk fitur:

- MULTI-SEND
- ENCRYPT
- DECRYPT
- PRIVATE TRANSFER
- CLAIM

Dengan sistem retry otomatis dan jeda antar proses agar semua transaksi **berhasil dikirim dengan stabil**.

---

## 📦 Fitur Utama

| Fitur               | Deskripsi                                                                 |
|--------------------|---------------------------------------------------------------------------|
| 🔁 MULTI-SEND       | Kirim ke banyak penerima dari file `p.txt`, jeda 15 detik per transaksi   |
| 🔐 ENCRYPT          | Enkripsi 5 OCT, retry hingga sukses, jeda 20 detik setelah berhasil       |
| 🔓 DECRYPT          | Dekripsi 1 OCT, retry hingga sukses, jeda 20 detik setelah berhasil       |
| 🕵️ PRIVATE TRANSFER | Kirim privat 0.1 OCT ke tiap penerima, jeda 60 detik per transaksi        |
| 📥 CLAIM            | Klaim semua private transfer masuk, retry setiap ID hingga berhasil       |

---

## ✍️ Format File 

### `wallet.txt`
Daftar wallet yang akan digunakan, ```address1|||priavtekey1```:
```sh
octraAddress1|||privateKey1
octraAddress2|||privateKey2
```

### `p.txt`
Daftar penerima + jumlah OCT:
```sh
octraReceiver1 0.5
octraReceiver2 1.25
```

---

## ▶️ Cara Menjalankan

### Aktifkan environment, dan pastikan codespace/VPS sudah install octra yang original:
```bash
git clone https://github.com/kenjisubagja/octraV2
```
```bash
python3 -m venv venv
source venv/bin/activate
```
✅ Sistem Retry Otomatis
Setiap langkah akan:

Retry otomatis jika gagal (misalnya nonce conflict, "no public key", dll)

Menunggu beberapa detik sebelum mencoba ulang

Tidak lanjut ke proses berikutnya sebelum transaksi sukses
## 👤
Created By Kenjisubagja:

**Kenji Subagja**  
📨 Telegram: [@kenjisubagja](https://t.me/kenjisubagja)  
🐦 Twitter/X: [@kenjisubagja](https://x.com/kenjisubagja)



