#!/usr/bin/env python3
import asyncio, json, re, os, time
from cli import ld, st, mk, snd, encrypt_balance, decrypt_balance, create_private_transfer, claim_private_transfer, get_pending_transfers

μ = 1_000_000
b58 = re.compile(r"^oct[1-9A-HJ-NP-Za-km-z]{44}$")

async def load_recipients(file_path='p.txt'):
    if not os.path.exists(file_path):
        print(f"[ERROR] File {file_path} not found.")
        return []
    with open(file_path) as f:
        lines = f.readlines()
    rcp = []
    for line in lines:
        parts = line.strip().split()
        if len(parts) == 2 and b58.match(parts[0]):
            try:
                amount = float(parts[1])
                rcp.append((parts[0], amount))
            except:
                continue
    return rcp

async def multi_send_from_file():
    print("[*] Menjalankan multi-send...")
    rcp = await load_recipients()
    if not rcp:
        print("[SKIP] Tidak ada penerima valid.")
        return
    n, b = await st()
    if n is None:
        print("[SKIP] Gagal ambil nonce.")
        return
    current_nonce = n + 1
    for to, a in rcp:
        try:
            t, _ = mk(to, a, current_nonce)
            ok, res, *_ = await snd(t)
            if ok:
                print(f"[✓] TX ke {to} ({a} OCT) sukses: {res[:12]}...")
            else:
                print(f"[✗] TX ke {to} gagal: {res}, lewati ke nonce berikutnya...")
        except Exception as e:
            print(f"[!] Exception TX ke {to}: {e}, lewati ke nonce berikutnya...")
        current_nonce += 1
        await asyncio.sleep(15)

async def do_encrypt():
    print("[*] Enkripsi 5 OCT...")
    while True:
        ok, res = await encrypt_balance(5)
        if ok:
            print(f"[✓] Enkripsi berhasil: {res.get('tx_hash', '')[:12]}...")
            break
        else:
            print(f"[✗] Gagal enkripsi: {res.get('error', res)}, retry dalam 25 detik...")
        await asyncio.sleep(25)
    await asyncio.sleep(20)

async def do_decrypt():
    print("[*] Dekripsi 1 OCT...")
    while True:
        ok, res = await decrypt_balance(1)
        if ok:
            print(f"[✓] Dekripsi berhasil: {res.get('tx_hash', '')[:12]}...")
            break
        else:
            print(f"[✗] Gagal dekripsi: {res.get('error', res)}, retry dalam 1 menit...")
        await asyncio.sleep(60)
    await asyncio.sleep(20)

async def do_private_send():
    print("[*] Kirim privat 0.1 OCT...")
    rcp = await load_recipients()
    for to, _ in rcp:
        while True:
            ok, res = await create_private_transfer(to, 0.1)
            if ok:
                print(f"[✓] Private TX ke {to[:12]}... sukses: {res.get('tx_hash', '')[:12]}...")
                break
            else:
                print(f"[✗] Gagal private TX ke {to[:12]}...: {res.get('error', res)}, retry dalam 30 detik...")
            await asyncio.sleep(30)
        await asyncio.sleep(60)

async def do_claim():
    print("[*] Claim transfer privat...")
    while True:
        transfers = await get_pending_transfers()
        if not transfers:
            print("[✓] Tidak ada transfer privat yang bisa diklaim.")
            break
        total = 0
        for t in transfers:
            while True:
                ok, res = await claim_private_transfer(t['id'])
                if ok:
                    print(f"[✓] Claim #{t['id']} sukses")
                    total += 1
                    break
                else:
                    print(f"[✗] Claim #{t['id']} gagal: {res.get('error', res)}, retry dalam 5 detik...")
                await asyncio.sleep(5)
        print(f"[✓] Total claimed: {total}")
        await asyncio.sleep(10)

async def main():
    if not ld():
        print("[!] Gagal load wallet.")
        return
    await multi_send_from_file()
    await do_encrypt()
    await do_decrypt()
    await do_private_send()
    await do_claim()

if __name__ == "__main__":
    print("🚀 Menjalankan auto_runner...")
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n⛔️ Dibatalkan oleh user.")
