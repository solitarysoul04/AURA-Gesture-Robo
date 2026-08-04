import cv2
import mediapipe as mp
import serial
import time
import numpy as np
import math

# Configuration
COM_PORT = 'COM3'         # Base Station Nano port
ESP32_IP = '192.168.1.50' # ESP32-CAM IP Address
URL = f"http://{ESP32_IP}:81/stream"

# Arduino Connection
try:
    arduino = serial.Serial(COM_PORT, 115200, timeout=1)
    time.sleep(2)
except Exception as e:
    print(f"Serial Error: {e}")
    arduino = None

cap_webcam = cv2.VideoCapture(0)
cap_rover = cv2.VideoCapture(URL)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

last_cmd_time = 0

def get_direction(hand_landmarks):
    tips = [8, 12, 16, 20]
    pips = [6, 10, 14, 18]
    fingers_up = []
    
    fingers_up.append(1 if hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x else 0)

    for i in range(4):
        fingers_up.append(1 if hand_landmarks.landmark[tips[i]].y < hand_landmarks.landmark[pips[i]].y else 0)
            
    if fingers_up == [0, 1, 0, 0, 0]: return 'F'  # Index up -> Forward
    if fingers_up == [0, 1, 1, 0, 0]: return 'B'  # Index + Middle up -> Backward
    if fingers_up == [1, 1, 0, 0, 0]: return 'L'  # Thumb + Index up -> Left
    if fingers_up == [1, 1, 1, 0, 0]: return 'R'  # Thumb + Index + Middle up -> Right
    return 'S' # Default -> Stop

def get_throttle(hand_landmarks):
    x1, y1 = hand_landmarks.landmark[4].x, hand_landmarks.landmark[4].y
    x2, y2 = hand_landmarks.landmark[8].x, hand_landmarks.landmark[8].y
    
    dist = math.hypot(x2 - x1, y2 - y1)
    speed = np.interp(dist, [0.05, 0.25], [0, 255])
    return int(np.clip(speed, 0, 255))

while True:
    ret1, frame_webcam = cap_webcam.read()
    ret2, frame_rover = cap_rover.read()
    if not ret1: break

    frame_webcam = cv2.flip(frame_webcam, 1) 
    rgb_frame = cv2.cvtColor(frame_webcam, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)
    
    cmd_char = 'S'
    speed_val = 0

    if result.multi_hand_landmarks and result.multi_handedness:
        for idx, hand_handedness in enumerate(result.multi_handedness):
            label = hand_handedness.classification[0].label 
            hand_landmarks = result.multi_hand_landmarks[idx]
            mp_draw.draw_landmarks(frame_webcam, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            if label == "Right": speed_val = get_throttle(hand_landmarks)
            elif label == "Left": cmd_char = get_direction(hand_landmarks)

    if time.time() - last_cmd_time > 0.1: 
        if arduino:
            payload = f"{cmd_char},{speed_val}\n"
            arduino.write(payload.encode())
        last_cmd_time = time.time()

    # Dashboard
    h, w = 480, 640
    frame_webcam = cv2.resize(frame_webcam, (w, h))
    
    if ret2:
        frame_rover = cv2.resize(frame_rover, (w, h))
    else:
        frame_rover = np.zeros((h, w, 3), dtype=np.uint8)
        cv2.putText(frame_rover, "Wi-Fi FPV LOST", (180, 240), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

    stats_panel = np.zeros((h, 300, 3), dtype=np.uint8)
    cv2.putText(stats_panel, "AURA CMD CENTER", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,255), 2)
    cv2.putText(stats_panel, f"DIR: {cmd_char}", (20, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 2)
    cv2.putText(stats_panel, f"PWR: {speed_val}", (20, 160), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,255), 2)
    
    # Throttle Bar
    bar_height = int(np.interp(speed_val, [0, 255], [0, 200]))
    cv2.rectangle(stats_panel, (50, 400), (100, 400 - bar_height), (0, 255, 255), cv2.FILLED)
    cv2.rectangle(stats_panel, (50, 400), (100, 200), (255, 255, 255), 2)
    
    # Final Dashboard
    dashboard = cv2.hconcat([frame_webcam, frame_rover, stats_panel])
    cv2.imshow("AURA Telemetry Interface", dashboard)
    
    # Press 'q' to safely exit
    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap_webcam.release()
cap_rover.release()
cv2.destroyAllWindows()
if arduino: arduino.close()
