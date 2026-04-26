# Python AI Experiments 🚀

Kumpulan project eksperimen Python berbasis AI dan Computer Vision.

# 1. AI Push-Up Counter
Program ini menggunakan MediaPipe untuk menghitung repetisi push-up secara otomatis melalui kamera.
# Fitur:
- Deteksi pose tubuh secara real-time.
- Logika "Anti-Cheating" (Hanya menghitung jika posisi badan horisontal).
- Auto-save riwayat ke file `.txt`.

# 02. Multi-Finger Hand Grab Counter
Program penghitung genggaman tangan menggunakan Hand Tracking.
# Fitur: 
- Deteksi akurat (harus 4 jari menutup), menghindari salah hitung saat hanya satu jari menekuk.
# Logika: 
- Memvalidasi status `folded` pada landmark jari Telunjuk, Tengah, Manis, dan Kelingking.

### Cara Install:
1. Clone repo ini.
2. Buat Virtual Environment: `python -m venv .venv`
3. Aktifkan venv: `.venv\Scripts\activate`
4. Install library: `pip install -r requirements.txt`

### Cara Menjalankan:
Jalankan file utama:
```bash
python 01-pushup-counter/pushup.py