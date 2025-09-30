# 🛠️ Wallet Tracker (Multi-Chain & Telegram Bot)

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![GitHub Actions](https://img.shields.io/github/actions/workflow/status/Rawna22/wallet-tracker/tracker.yml?branch=main)
![Stars](https://img.shields.io/github/stars/Rawna22/wallet-tracker?style=social)

Script Python sederhana untuk cek saldo wallet multi-chain (Ethereum, Base, zkSync, Optimism, Soneium) + notifikasi otomatis ke **Telegram Bot** 📲  

---

## ✨ Fitur
- 🔎 **Cek saldo native ETH** di beberapa chain (Ethereum, Base, zkSync, Optimism, Soneium)  
- 💰 **Ambil saldo token ERC-20** via [Covalent API](https://www.covalenthq.com/)  
- 📜 **Lihat riwayat transaksi wallet**  
- 🤖 **Kirim ringkasan otomatis ke Telegram** (opsional)  
- ⚡ Bisa dijalankan **manual** atau **otomatis via GitHub Actions**  

---

## ⚡ Demo Screenshot
> Tampilan hasil script di Codespaces

![Demo](./assets/demo.png)

## 🚀 Instalasi Cepat

```bash
git clone https://github.com/Rawna22/multi-wallet-dashboard
cd multi-wallet-dashboard
pip install -r requirements.txt
```

📌 Roadmap

```bash
[ ] Integrasi lebih banyak chain (Arbitrum, Polygon)
[ ] Export laporan ke PDF/CSV
[ ] Support notifikasi Telegram (seperti repo sebelumnya)
[ ] Deploy ke Streamlit Cloud (biar bisa diakses publik)
```

## 🔑 Konfigurasi .env
Buat file .env di root folder:

```bash
# RPC endpoints
ETHEREUM_RPC=https://mainnet.infura.io/v3/YOUR_INFURA_KEY
BASE_RPC=https://mainnet.base.org
ZKSYNC_RPC=https://zksync2-mainnet.zksync.io
OPTIMISM_RPC=https://mainnet.optimism.io
SONEIUM_RPC=https://rpc.soneium.org

# Covalent API
COVALENT_API_KEY=ckey_xxxxxxxxxxxxxxxxxxxxx

# Telegram Bot (opsional)
TELEGRAM_BOT_TOKEN=123456:ABCdefGhIjklMNop
TELEGRAM_CHAT_ID=987654321

# Wallet address
WALLET_ADDRESS=0x2e5392f3d727a5c0e5a2e4a3530c2254dbce205d
```

---

## ▶️ Menjalankan Script

```bash
streamlit run app.py
```
Kemudian buka browser:
👉 https://streamlit.io

---


## 📌 Todo / Next Features
```bash
[ ] Multi-wallet support (portfolio total + breakdown per chain)
[ ] Dashboard Web (Flask/Streamlit) untuk grafik portofolio
[ ] Export laporan ke CSV/Excel
[ ] Integrasi notifikasi Discord
```

## 📄 License
MIT © Rawna22

👉 README ini sudah:  
- Ada **badges** (Python, License, Actions, Stars)  
- Ada **demo screenshot section**  
- Ada **Fitur, Instalasi, Usage, Workflow, Todo list**  

Mau saya bikinkan **versi yang sudah langsung dalam file `README.md`** biar bisa kamu commit langsung?
