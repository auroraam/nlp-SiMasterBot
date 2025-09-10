import sys, os, subprocess, time
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from engine import reply


def test_greetings():
    assert "halo" in reply("halo simaster").lower()
    assert "bantu" in reply("hii, mau tanya dong").lower()


def test_thankyou():
    assert "sama-sama" in reply("terima kasih").lower()
    assert "sama-sama" in reply("makasiiiii").lower()
    assert "sama-sama" in reply("thanks").lower()
    assert "sama-sama" in reply("thank youuu").lower()


def test_login():
    assert "login" in reply("gimana cara login simaster").lower()


def test_access():
    out = reply("cara akses aplikasi simaster")
    assert "website" in out.lower() or "aplikasi" in out.lower()


def test_password():
    assert "password" in reply("aku lupa password simaster").lower()


def test_presensi():
    assert "presensi" in reply("cara absen qr code").lower()


def test_kehadiran():
    assert "kehadiran" in reply("lihat persentase kehadiran saya").lower()


def test_jadwal_kuliah():
    assert "jadwal" in reply("lihat jadwal kuliah hari ini").lower()


def test_jadwal_ujian():
    assert "ujian" in reply("jadwal UTS kapan?").lower()


def test_nilai():
    assert "nilai" in reply("cara lihat nilai").lower()
    assert "transkrip" in reply("lihat transkrip saya").lower()


def test_krs():
    assert "krs" in reply("cara isi krs").lower()


def test_ektm():
    assert "ektm" in reply("dimana lihat ktm").lower()


def test_akademik():
    assert "akademik" in reply("menu akademik apa saja").lower()


def test_error():
    assert "error" in reply("simaster tidak bisa akses").lower()


def test_update():
    assert "versi" in reply("apakah ada update aplikasi").lower()


def test_fitur():
    assert "layanan" in reply("fitur apa saja di simaster").lower()


def test_helpdesk():
    assert "helpdesk" in reply("butuh bantuan hubungi siapa").lower()


def test_website():
    assert "https://simaster.ugm.ac.id" in reply("link simaster resmi").lower()


def test_download():
    assert "aplikasi" in reply("dimana download apk simaster").lower()


def test_evaluasi():
    assert "evaluasi" in reply("cara isi evaluasi dosen").lower()


def test_perpus():
    assert "perpustakaan" in reply("cara pinjam buku perpus").lower()


def test_registrasi():
    assert "akun" in reply("belum punya akun simaster").lower()


def test_fallback():
    assert "faq" in reply("qwertyuiop").lower()

def test_case_insensitive():
    assert "KRS" in reply("IsI KrS")
    assert "Nilai" in reply("NILAI")

def test_logging_creates_file():
    reply("halo")
    assert os.path.exists("logs/bot.log")

def test_cli_runs():
    result = subprocess.run(
        ["python", "cli.py"],
        input="password\n:q\n",   
        text=True,
        capture_output=True,
        encoding="utf-8",
        errors="replace"
    )
    assert "halo" in result.stdout.lower() or "faq" in result.stdout.lower()

def test_variants():
    assert "password" in reply("lupaa kata sandiiiii").lower()
    assert "presensi" in reply("scan qr code").lower()
    assert "sama-sama" in reply("makasiiiii").lower()

def test_performance():
    start = time.time()
    for _ in range(1000):
        reply("lupa password")
    end = time.time()
    assert (end - start) < 1

def test_empty_input():
    out = reply("")
    assert isinstance(out, str)