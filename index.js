// index.js
import qrcode from "qrcode-terminal";
import { spawn } from "child_process";
import dotenv from "dotenv";
import pkg from "whatsapp-web.js";

const { Client, LocalAuth } = pkg;
import fs from "fs";

dotenv.config();

const pythonPath = process.env.PYTHON_BIN || "python"; // gunakan .env jika mau

// buat client WA dengan LocalAuth supaya session tersimpan
const client = new Client({
  authStrategy: new LocalAuth({ clientId: "simaster-bot" })
});

client.on("qr", (qr) => {
  console.log("[WA] Scan QR berikut untuk login:");
  qrcode.generate(qr, { small: true });
});

client.on("ready", () => {
  console.log("[WA] Client siap.");
});

client.on("message", async (message) => {
  try {
    // ignore pesan dari bot sendiri
    if (message.fromMe) return;

    // kalau pesan tidak berisi teks, skip (kamu bisa handle media jika mau)
    const text = message.body || "";
    if (!text.trim()) {
      await message.reply("Maaf, aku hanya bisa merespon pesan teks saat ini.");
      return;
    }

    console.log("[WA] Pesan masuk:", text);

    // spawn python process dan kirim teks via stdin
    const py = spawn(pythonPath, ["reply_cli.py"], {
      cwd: process.cwd(),
      stdio: ["pipe", "pipe", "pipe"]
    });

    let stdout = "";
    let stderr = "";

    py.stdout.on("data", (chunk) => {
      stdout += chunk.toString();
    });
    py.stderr.on("data", (chunk) => {
      stderr += chunk.toString();
    });

    py.on("error", (err) => {
      console.error("[WA] Gagal spawn python:", err);
    });

    py.on("close", async (code) => {
      if (stderr) console.error("[PY STDERR]", stderr);
      if (!stdout) {
        console.error("[WA] Python tidak mengembalikan output.");
        await message.reply("Maaf, terjadi error pada engine.");
        return;
      }
      try {
        const obj = JSON.parse(stdout);
        const replyText = obj && obj.reply ? obj.reply : "Maaf, saya belum bisa menjawab itu.";
        console.log("[WA] Reply:", replyText);
        await message.reply(replyText);
      } catch (e) {
        console.error("[WA] Gagal parsing JSON dari Python:", e, "raw:", stdout);
        await message.reply("Maaf, terjadi error saat memproses jawaban.");
      }
    });

    // kirim teks ke stdin python dan akhiri
    py.stdin.write(text);
    py.stdin.end();

  } catch (err) {
    console.error("[WA] Error handler:", err);
  }
});

// inisialisasi client
client.initialize();
