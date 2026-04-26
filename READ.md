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

# 03. AI Anti-Drowsiness Detector
Program pendeteksi kantuk real-time menggunakan webcam dan Face Mesh Tracking.

# Fitur:
- Deteksi mata tertutup terlalu lama (sleep detection).
- Deteksi menguap berdasarkan bukaan mulut.
- Deteksi kepala menunduk sebagai indikasi tertidur.
- Alarm suara custom otomatis berulang saat terdeteksi ngantuk.
- Tampilan status realtime di layar webcam.

# Logika:
- Menghitung `EAR (Eye Aspect Ratio)` dari landmark mata untuk mendeteksi mata merem.
- Menghitung `MAR (Mouth Aspect Ratio)` dari landmark mulut untuk mendeteksi nguap.
- Membandingkan jarak landmark hidung dan dagu untuk mendeteksi kepala nunduk.
- Jika nilai melebihi threshold beberapa frame berturut-turut, sistem mengaktifkan alarm hingga kondisi normal kembali.


### Cara Menjalankan:
Jalankan file utama:
```bash
python 01-pushup-counter/pushup.py