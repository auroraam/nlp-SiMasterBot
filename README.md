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
deactivate
```

### 3. Setup Node.js (Integrasi WhatsApp)
Install dependencies:
```bash
npm install
```

### ▶️ Run
## Mode CLI (Terminal)
Jalankan bot langsung di terminal:
```bash
.venv\Scripts\activate      # Windows
# source .venv/bin/activate # Linux/Mac
python cli.py
```

## Mode WhatsApp
1. Pastikan .env sudah diset sesuai .env.example.
2. Siapkan no wa yang akan digunakan sebagai bot.
3. Jalankan integrasi:
```bash
node index.mjs
```
3. Scan QR code dengan WhatsApp di device tersebut.
4. Bot akan otomatis membalas chat mengenai FAQ SIMASTER.

### 🔑 Konfigurasi Environment
Buat file .env (jangan di-commit). Contoh ada di .env.example:
```env
# Path ke Python (ubah sesuai OS)
# Windows:
PYTHON_BIN=.venv/Scripts/python.exe
# Linux/Mac:
# PYTHON_BIN=.venv/bin/python3
```

### 🧪 Testing
Jalankan unit test (pytest):
```bash
.venv\Scripts\activate      # Windows
# source .venv/bin/activate # Linux/Mac
pytest -q
```
Berikut contoh hasil testing:
```bash
(.venv) PS C:\Users\hp\source\repos\nlp last\nlp-simaster-bot> pytest -q
.......                                                              [100%]
7 passed in 0.09s
```

### Struktur Proyek
Berikut adalah struktur proyek SiMasterBot
```bash
│   .env.example
│   .gitignore
│   cli.py # untuk menjalankan bot di terminal
│   engine.py # logic
│   index.mjs
│   package-lock.json
│   package.json
│   README.md
│   reply_cli.py # untuk menghubungkan logic python dengan node js
│   requirements.txt
├───logs
│       bot.log
└───tests
        test_engine.py
```

### Log
Bot memiliki log yang digunakan untuk menyimpan histori prompt yang masuk. Beberapa contoh dari log;
```bash
2025-09-10 16:12:45,050 [INFO] Input: halo → Reply: Maaf, pertanyaanmu belum ada di FAQ. Cek portal Simaster atau hubungi admin.
2025-09-10 16:13:11,874 [INFO] Input: aku lupa password euy, gmn yah cara gantinya → Reply: Jika lupa password, tekan tombol 'Lupa Kata Sandi' di login page SIMASTER, lalu cek email mahasiswa.
2025-09-10 16:20:05,051 [INFO] Input: persentase → Reply: Maaf, pertanyaanmu belum ada di FAQ. Cek portal Simaster atau hubungi admin.
2025-09-10 16:20:14,615 [INFO] Input: persentase absen → Reply: Untuk presensi, pilih menu Perkuliahan → Presensi → scan QR code di kelas. Aktifkan GPS. Jika gagal, gunakan menu Klaim Presensi.
2025-09-10 16:26:00,563 [INFO] Input: terimakasiii → Reply: Sama-sama! Semoga membantu ya. 👍
```

---

Selamat mencoba SiMasterBot, semoga membantu!
Pengembang: Aurora Ma'isyah & Nabila Puspita Dewi
