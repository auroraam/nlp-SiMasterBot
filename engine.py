import os
import re
import logging
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(BASE_DIR, "logs")
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    filename="logs/bot.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    encoding="utf-8"  # biar emoji/karakter non-ASCII aman
)

RULES = [
    (re.compile(r"\b(login|log\s*in|masuk|sign\s*in)\b", re.I),
     "Untuk login SIMASTER UGM gunakan akun SSO UGM (email mahasiswa/dosen + password)."),
    
    (re.compile(r"\b(error|tidak\s+bisa\s+akses|gagal\s+login|aplikasi\s+tidak\s+jalan|trouble|masalah)\b", re.I),
     "Coba clear cache, ganti device, logout-login ulang, atau update ke versi terbaru. Jika masih error, hubungi helpdesk UGM."),

    (re.compile(r"\b(update|versi\s+baru|upgrade\s+aplikasi)\b", re.I),
     "Versi terbaru SIMASTER tersedia di Google Play Store & App Store."),

    (re.compile(r"\b(akses|buka|open|download|install|unduh|apk|aplikasi|app)\b", re.I),
     "SIMASTER dapat diakses via website https://simaster.ugm.ac.id atau aplikasi mobile (Google Play Store / App Store)."),

    (re.compile(r"\b(lupa+\s+(?:passwo+r+d+|kata\s*sa+nd+i+)|reset\s+(?:password|kata\s*sandi))\b", re.I),
     "Jika lupa password, tekan tombol 'Lupa Kata Sandi' di login page SIMASTER, lalu cek email mahasiswa."),

    (re.compile(r"\b(presensi|absen|absensi|hadir|qr\s*code|scan\s*qr|qr)\b", re.I),
     "Untuk presensi, pilih menu Perkuliahan → Presensi → scan QR code di kelas. Aktifkan GPS. Jika gagal, gunakan menu Klaim Presensi."),

    (re.compile(r"\b(persentase\s+kehadiran|rekap\s+hadir|jumlah\s+hadir|prosentase\s+absen)\b", re.I),
     "Persentase kehadiran mahasiswa dapat diakses melalui menu Perkuliahan → Kehadiran Mahasiswa."),

    (re.compile(r"\b(jadwal\s+(?:kuliah|kelas)|ruang\s+kuliah|jam\s+kuliah|jadwal\s+hari\s+ini)\b", re.I),
     "Jadwal dan ruang kuliah dapat dilihat di menu Akademik → Jadwal Kuliah, juga tampil di beranda aplikasi."),

    (re.compile(r"\b(jadwal\s+(?:ujian|uts|uas|tes)|uji\s*coba)\b", re.I),
     "Jadwal ujian tersedia di menu Akademik → Jadwal Ujian."),

    (re.compile(r"\b(nilai|transkrip|khs|ipk|hasil\s*studi|daftar\s*nilai)\b", re.I),
     "Nilai dapat diakses di Akademik → Hasil Studi/Transkrip. KHS/transkrip sementara bisa diunduh langsung di SIMASTER."),

    (re.compile(r"\b(krs|isi\s+krs|pengisian\s+krs|ambil\s+mata\s*kuliah|perwalian)\b", re.I),
     "Pengisian KRS dilakukan di menu Akademik → KRS sesuai jadwal. Pastikan sudah perwalian dengan dosen pembimbing."),

    (re.compile(r"\b(ektm|ktm|kartu\s+tanda\s+mahasiswa)\b", re.I),
     "eKTM bisa diakses di menu Akademik → eKTM. Unduh via portal web, klik kanan gambar → Save image as..."),

    (re.compile(r"\b(akademik|menu\s+akademik)\b", re.I),
     "Menu Akademik mencakup: jadwal kuliah, nilai, KRS, eKTM, dll."),

    (re.compile(r"\b(fitur|menu|layanan|apa\s+saja|apa\s+yang\s+ada)\b", re.I),
     "SIMASTER menyediakan layanan: akademik, jadwal, nilai, presensi, penelitian, pengabdian, hingga info fasilitas kampus."),

    (re.compile(r"\b(bantuan|helpdesk|kontak|hubungi|call\s*center|cs|support)\b", re.I),
     "Untuk bantuan hubungi helpdesk UGM: email helpdesk@ugm.ac.id atau telp (0274) 6491919."),

    (re.compile(r"\b(web\s+simaster|link\s+simaster|website\s+simaster)\b", re.I),
     "Portal resmi SIMASTER: https://simaster.ugm.ac.id"),

    (re.compile(r"\b(download\s+aplikasi|apk|unduh\s+simaster|install\s+simaster)\b", re.I),
     "Aplikasi resmi SIMASTER tersedia di Google Play Store dan Apple App Store."),

    (re.compile(r"\b(evaluasi\s+dosen|penilaian\s+dosen|survey\s+dosen)\b", re.I),
     "Evaluasi dosen dapat dilakukan melalui menu Perkuliahan → Evaluasi Dosen."),

    (re.compile(r"\b(perpus|perpustakaan|koleksi|buku|peminjaman|pinjam|booking\s+tempat|reservasi\s+kursi)\b", re.I),
     "Perpustakaan SIMASTER: cari koleksi, lihat detail lokasi buku, pesan kursi, pinjam buku, dll melalui menu Perpustakaan."),

    (re.compile(r"\b(belum\s+punya\s+akun|buat\s+akun|registrasi|daftar\s+akun)\b", re.I),
     "Buat akun di https://simaster.ugm.ac.id → klik 'Registrasi Akun'."),

    (re.compile(r"\b(halo+|hai+|hello+|hi+|hei|hola|hallo)\b", re.I),
     "Halo! Ada yang bisa saya bantu terkait SIMASTER? 😊"),

    (re.compile(r"\b(terima\s?kasi+h*i*|makasi+h*i*|thanks+|thank\s*you+)\b", re.I),
     "Sama-sama! Semoga membantu ya. 👍"),
]


def reply(text: str) -> str:
    for pattern, ans in RULES:
        if pattern.search(text):
            logging.info(f"Input: {text} → Reply: {ans}")
            return ans
    fallback = "Maaf, pertanyaanmu belum ada di FAQ. Cek portal Simaster atau hubungi admin."
    logging.info(f"Input: {text} → Reply: {fallback}")
    return fallback