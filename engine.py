import re
from datetime import datetime

RULES = [
    (re.compile(r"\b(lupa password|reset password)\b", re.I),
     "Klik 'Lupa Password' di halaman login Simaster, lalu cek email mahasiswa."),
    (re.compile(r"\b(krs|isi krs)\b", re.I),
     "Masuk ke Simaster → Menu Akademik → KRS → Tambah Mata Kuliah."),
    (re.compile(r"\b(jadwal kuliah|lihat jadwal)\b", re.I),
     "Jadwal kuliah ada di Simaster → Menu Akademik → Jadwal Perkuliahan."),
    (re.compile(r"\b(nilai|khs|transkrip)\b", re.I),
     "Nilai bisa dilihat di Simaster → Menu Akademik → KHS."),
    (re.compile(r"\b(kkn|skripsi)\b", re.I),
     "Pendaftaran KKN/Skripsi ada di Simaster → Menu KKN/Skripsi."),
]

def reply(text: str) -> str:
    for pattern, ans in RULES:
        if pattern.search(text):
            return ans
    return "Maaf, pertanyaanmu belum ada di FAQ. Cek portal Simaster atau hubungi admin."
