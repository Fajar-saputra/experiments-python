# ============================================
# AI ANTI NGANTUK FINAL BOSS + SUARA "FAAH"
# Fitur:
# - Deteksi mata merem lama
# - Deteksi mulut nguap
# - Deteksi kepala nunduk
# - Alarm suara TTS: "FAAH BANGUN WOI!"
# - Tampilan realtime webcam
# Tekan Q untuk keluar
# ============================================

import cv2
import mediapipe as mp
import math
import threading
import pyttsx3
import pygame
import random

# ---------- INIT ----------
mp_face = mp.solutions.face_mesh
face_mesh = mp_face.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

cap = cv2.VideoCapture(0)

# Text To Speech
engine = pyttsx3.init()
engine.setProperty('rate', 160)   # kecepatan bicara
engine.setProperty('volume', 1.0)

alarm_active = False

# ---------- FUNGSI ----------


# baru
pygame.mixer.init()
pygame.mixer.music.set_volume(1.0) 

sounds = [
    "faah.mp3",
]

pygame.mixer.init()

sounds = ["faah.mp3"]

alarm_playing = False

def play_alarm_loop():
    global alarm_playing

    if not alarm_playing:
        alarm_playing = True

        file = random.choice(sounds)
        pygame.mixer.music.load(file)
        pygame.mixer.music.play(-1)   # loop terus

def stop_alarm():
    global alarm_playing

    pygame.mixer.music.stop()
    alarm_playing = False
# =====

# def speak_alarm():
def speak_alarm():
    global alarm_active
    if not alarm_active:
        alarm_active = True
        engine.say("FAAH! Bangun woi! Jangan tidur!")
        engine.runAndWait()
        alarm_active = False

def distance(p1, p2):
    return math.hypot(p2.x - p1.x, p2.y - p1.y)

# Counter
sleep_counter = 0
yawn_counter = 0
head_counter = 0

# ---------- LOOP ----------
while True:
    ret, frame = cap.read()
    if not ret:
        break

    h, w, _ = frame.shape
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb)

    status = "AMAN"

    if results.multi_face_landmarks:
        face = results.multi_face_landmarks[0]
        lm = face.landmark

        # ======================
        # 1. DETEKSI MATA MEREM
        # ======================
        top_eye = lm[159]
        bottom_eye = lm[145]
        left_eye = lm[33]
        right_eye = lm[133]

        eye_vertical = distance(top_eye, bottom_eye)
        eye_horizontal = distance(left_eye, right_eye)

        ear = eye_vertical / eye_horizontal

        # ======================
        # 2. DETEKSI NGUAP
        # ======================
        top_mouth = lm[13]
        bottom_mouth = lm[14]
        left_mouth = lm[78]
        right_mouth = lm[308]

        mouth_vertical = distance(top_mouth, bottom_mouth)
        mouth_horizontal = distance(left_mouth, right_mouth)

        mar = mouth_vertical / mouth_horizontal

        # ======================
        # 3. DETEKSI KEPALA NUNDUK
        # ======================
        nose = lm[1]
        chin = lm[152]

        head_drop = chin.y - nose.y

        # ======================
        # LOGIKA
        # ======================

        # Mata merem
        if ear < 0.20:
            sleep_counter += 1
        else:
            sleep_counter = 0

        # Nguap
        if mar > 0.60:
            yawn_counter += 1
        else:
            yawn_counter = 0

        # Kepala turun
        if head_drop > 0.38:
            head_counter += 1
        else:
            head_counter = 0

        # Trigger alarm
        if sleep_counter > 8:
            status = "MATA MEREM!"
        elif yawn_counter > 8:
            status = "NGUAP PARAH!"
        elif head_counter > 15:
            status = "KEPALA NUNDUK!"
        else:
            status = "AMAN"

        if status != "AMAN":
            play_alarm_loop()
        else:
            stop_alarm()
            

        # Display data
        cv2.putText(frame, f"EAR: {ear:.2f}", (20,40),
                    cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,255,0),2)

        cv2.putText(frame, f"MAR: {mar:.2f}", (20,70),
                    cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,0),2)

        cv2.putText(frame, status, (20,120),
                    cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)

    cv2.imshow("AI ANTI NGANTUK FINAL BOSS", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()