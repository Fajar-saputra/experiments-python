import cv2
import mediapipe as mp
import time
import math

mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils
pose = mp_pose.Pose(min_detection_confidence=0.7, min_tracking_confidence=0.7)

counter = 0
stage = "up"

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret: break

    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(image)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    if results.pose_landmarks:
        landmarks = results.pose_landmarks.landmark
        
        # 1. Ambil koordinat penting
        nose = landmarks[mp_pose.PoseLandmark.NOSE.value]
        shoulder = landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value]
        hip = landmarks[mp_pose.PoseLandmark.LEFT_HIP.value]
        
        # 2. LOGIKA VALIDASI: APAKAH SEDANG REBAHAN/HORISONTAL?
        # Kita cek selisih X antara Bahu dan Pinggang. 
        # Kalau berdiri, selisih X kecil. Kalau push-up (samping), selisih X besar.
        dist_x = abs(shoulder.x - hip.x)
        is_horizontal = dist_x > 0.2  # Threshold: badan harus memanjang secara horisontal
        
        # 3. LOGIKA HITUNGAN (Cuma jalan kalau is_horizontal True)
        if is_horizontal:
            # Gunakan perbandingan Y Hidung dan Y Bahu
            if nose.y > shoulder.y:
                if stage == "up":
                    stage = "down"
            
            if nose.y < (shoulder.y - 0.05) and stage == "down":
                stage = "up"
                counter += 1
                print(f"Push-up Sah! Total: {counter}")
        else:
            # Jika terdeteksi berdiri/jongkok
            cv2.putText(image, "POSISI SALAH: HARUS HORISONTAL", (10, 450), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)

        # UI Visual
        color = (0, 255, 0) if is_horizontal else (0, 0, 255)
        cv2.rectangle(image, (0,0), (250,80), (0,0,0), -1)
        cv2.putText(image, f'COUNT: {counter}', (10,60), 
                    cv2.FONT_HERSHEY_SIMPLEX, 2, color, 3)
        
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

    cv2.imshow('AI Push Up - Anti Standing Mode', image)
    if cv2.waitKey(10) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()

# Simpan ke TXT
with open("history_pushup.txt", "a") as f:
    f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Berhasil {counter} Reps\n")