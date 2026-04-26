# Python AI Experiments 🚀

Kumpulan project eksperimen Python berbasis AI dan Computer Vision.

## 1. AI Push-Up Counter
Program ini menggunakan MediaPipe untuk menghitung repetisi push-up secara otomatis melalui kamera.

### Fitur:
- Deteksi pose tubuh secara real-time.
- Logika "Anti-Cheating" (Hanya menghitung jika posisi badan horisontal).
- Auto-save riwayat ke file `.txt`.

### Cara Install:
1. Clone repo ini.
2. Buat Virtual Environment: `python -m venv .venv`
3. Aktifkan venv: `.venv\Scripts\activate`
4. Install library: `pip install -r requirements.txt`

### Cara Menjalankan:
Jalankan file utama:
```bash
python 01-pushup-counter/pushup.py