# reply_cli.py
#!/usr/bin/env python
import sys
import json
from engine import reply

def main():
    try:
        text = sys.stdin.read().strip()
        if not text:
            # tetap keluarkan JSON agar caller (Node) tidak stuck
            sys.stdout.reconfigure(encoding='utf-8')
            print(json.dumps({"reply": "", "rule": None}, ensure_ascii=False))
            return

        out = reply(text)
        # jika engine hanya mengembalikan string, bungkus jadi dict
        if isinstance(out, str):
            out = {"reply": out, "rule": None}

        # Pastikan stdout menggunakan UTF-8 supaya simbol unicode tidak error di Windows
        try:
            sys.stdout.reconfigure(encoding='utf-8')
        except Exception:
            # some older Pythons may not support; fallback: set environment var
            pass

        print(json.dumps(out, ensure_ascii=False))
    except Exception as e:
        sys.stdout.reconfigure(encoding='utf-8')
        print(json.dumps({"reply": f"Error: {e}", "rule": None}, ensure_ascii=False))

if __name__ == "__main__":
    main()
