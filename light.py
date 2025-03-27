import cv2
import mediapipe as mp
import serial
import time

ser = serial.Serial('COM5', 115200)  


mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)


cap = cv2.VideoCapture(0)


buttons = [(100, 100, 200, 150), (250, 100, 350, 150), (400, 100, 500, 150)]
labels = ["1", "2", "3"]  

prev_state = None  

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)
    
    detected = None  
    
    
    for (x1, y1, x2, y2), label in zip(buttons, labels):
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, label, (x1 + 10, y1 + 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
    
    
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            for id, lm in enumerate(hand_landmarks.landmark):
                h, w, _ = frame.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                
                if id == 8:  
                    cv2.circle(frame, (cx, cy), 10, (0, 0, 255), -1)
                    
                    for (x1, y1, x2, y2), label in zip(buttons, labels):
                        if x1 < cx < x2 and y1 < cy < y2:
                            detected = label
                            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), -1)
                            cv2.putText(frame, label, (x1 + 10, y1 + 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
                            break
            
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    
    
    if detected and detected != prev_state:
        print(f"Button {detected} Pressed")
        ser.write(detected.encode() + b'\n')
        prev_state = detected
    elif not detected and prev_state:
        print("No button detected")
        ser.write(b'0\n')  
        prev_state = None

    cv2.imshow("Finger Touch Buttons", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
ser.close()