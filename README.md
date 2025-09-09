# 🤖 SiMasterBot – FAQ Chatbot

Chatbot sederhana berbasis aturan (regex) untuk membantu mahasiswa mengakses informasi umum seputar **SIMASTER UGM**.  
Dibangun dengan **Python** (core bot) dan diintegrasikan ke **WhatsApp** menggunakan `whatsapp-web.js`.

---

## ⚙️ Setup

### 1. Clone Repository
```bash
git clone https://github.com/username/nlp-simaster-bot.git
cd nlp-simaster-bot
```

### 2. Setup Python
Buat virtual environment & install dependencies:
```bash
python -m venv .venv
.venv\Scripts\activate      # Windows
# source .venv/bin/activate # Linux/Mac

pip install -r requirements.txt
```

### 3. Setup Node.js (Integrasi WhatsApp)
Install dependencies:
```bash
npm install
```

### ▶️ Run
Mode CLI (Terminal)
Jalankan bot langsung di terminal:
```bash
python cli.py
```

### Mode WhatsApp
1. Pastikan .env sudah diset sesuai .env.example.
2. Jalankan integrasi:
```bash
node index.js
```
3. Scan QR code dengan WhatsApp di HP.
4. Bot akan otomatis membalas chat sesuai FAQ SIMASTER.

### 🔑 Konfigurasi Environment
Buat file .env (jangan di-commit). Contoh ada di .env.example:
```env
# Path ke Python (ubah sesuai OS)
# Windows:
PYTHON_BIN=.venv/Scripts/python.exe
# Linux/Mac:
# PYTHON_BIN=.venv/bin/python3

# (opsional) Client ID untuk multi-session WA
# CLIENT_ID=simaster-bot
```

### 🧪 Testing
Jalankan unit test (pytest):
```bash
pytest -q
```
