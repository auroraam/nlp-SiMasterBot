import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from engine import reply

def test_login():
    assert "login" in reply("gimana cara login simaster").lower()

def test_password():
    assert "password" in reply("aku lupa password simaster").lower()

def test_krs():
    assert "krs" in reply("cara isi krs").lower()

def test_jadwal():
    assert "jadwal" in reply("lihat jadwal kuliah").lower()

def test_nilai():
    assert "nilai" in reply("cara lihat nilai").lower()

def test_helpdesk():
    assert "helpdesk" in reply("butuh bantuan hubungi siapa").lower()

def test_fallback():
    assert "faq" in reply("qwertyuiop").lower()
