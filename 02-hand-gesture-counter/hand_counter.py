import cv2
import mediapipe as mp
import time

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

counter = 0
status = "terbuka"

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret: break

    frame = cv2.flip(frame, 1)
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(image)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            landmarks = hand_landmarks.landmark
            
            # Daftar titik ujung jari (tips) dan sendi tengah (mcp/pip)
            # 8:Telunjuk, 12:Tengah, 16:Manis, 20:Kelingking
            finger_tips = [8, 12, 16, 20]
            finger_mcp = [6, 10, 14, 18]
            
            fingers_folded = []
            
            for i in range(4):
                # Jika ujung jari lebih rendah dari sendinya, berarti menekuk
                if landmarks[finger_tips[i]].y > landmarks[finger_mcp[i]].y:
                    fingers_folded.append(True)
                else:
                    fingers_folded.append(False)

            # Syarat Genggam: KEEMPAT jari harus menekuk (True semua)
            if all(fingers_folded):
                if status == "terbuka":
                    status = "genggam"
                    counter += 1
                    print(f"Genggam Sah! Total: {counter}")
            
            # Syarat Terbuka: Minimal ada jari yang berdiri (False)
            elif not any(fingers_folded):
                status = "terbuka"

            # Gambar titik tangan
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    # Tampilkan UI
    cv2.rectangle(image, (0,0), (280, 80), (0,0,0), -1)
    cv2.putText(image, f'GRAB: {counter}', (10, 60), 
                cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,255), 3)

    cv2.imshow('Hand Gesture Counter', image)
    if cv2.waitKey(10) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()

# Simpan hasil
with open("history_hand.txt", "a") as f:
    f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Genggam: {counter} kali\n")