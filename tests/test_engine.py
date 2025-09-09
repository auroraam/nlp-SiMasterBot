from engine import reply

def test_password():
    assert "Lupa Password" in reply("aku lupa password simaster")

def test_krs():
    assert "KRS" in reply("cara isi krs")

def test_jadwal():
    assert "Jadwal" in reply("lihat jadwal kuliah")

def test_nilai():
    assert "Nilai" in reply("lihat nilai")

def test_kkn():
    assert "KKN" in reply("pendaftaran kkn kapan")

def test_fallback():
    assert "FAQ" in reply("qwertyuiop")
