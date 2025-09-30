# 📊 Multi-Wallet Web3 Portfolio Tracker
UI sederhana berbasis Streamlit untuk memantau saldo banyak wallet di beberapa chain (Ethereum, Base, zkSync, Optimism) + breakdown token via Covalent API.
Cocok untuk showcase portofolio Web3 kamu di GitHub 🚀

✨ Fitur
🔍 Multi-Wallet Tracking → bukan cuma 1, tapi list banyak wallet sekaligus.
🌐 Multi-Chain → dukung Ethereum, Base, zkSync, Optimism (bisa ditambah).
💰 Native Balance → tampilkan saldo ETH/chain langsung via Web3.
🪙 Token Portfolio → breakdown token ERC-20 via Covalent API.
📊 Visualisasi Data → bar chart total per chain + pie chart distribusi token.
⚡ Web UI → built with Streamlit, cepat & ringan.

🚀 Instalasi Cepat

git clone https://github.com/Rawna22/multi-wallet-dashboard
cd multi-wallet-dashboard
pip install -r requirements.txt

⚙️ Konfigurasi
nano .env

ETHEREUM_RPC=https://mainnet.infura.io/v3/YOUR_KEY
BASE_RPC=https://mainnet.base.org
ZKSYNC_RPC=https://zksync2-mainnet.zksync.io
OPTIMISM_RPC=https://mainnet.optimism.io
COVALENT_API_KEY=ckey_xxxxxxxxxxxxxxx

Tambahkan list wallet di file wallets.json:

{
  "Ethereum": [
    "0xYourWallet1",
    "0xYourWallet2"
  ],
  "Base": [
    "0xAnotherWallet"
  ],
  "zkSync": [
    "0xWalletZk"
  ],
  "Optimism": [
    "0xWalletOp"
  ]
}

▶️ Jalankan
streamlit run app.py

Kemudian buka browser:
👉 http://localhost:8501

📸 Preview
💻 Dashboard akan menampilkan:
Tabel saldo tiap wallet per chain
Total saldo per chain
Bar chart distribusi saldo antar chain
Pie chart distribusi token (ERC-20 via Covalent)

📌 Roadmap
[ ] Integrasi lebih banyak chain (Arbitrum, Polygon)
[ ] Export laporan ke PDF/CSV
[ ] Support notifikasi Telegram (seperti repo sebelumnya)
[ ] Deploy ke Streamlit Cloud (biar bisa diakses publik)
