# Gesture-Controlled LED System with ESP32

## 📌 Project Overview
This project implements a **gesture-based light control system** using OpenCV, MediaPipe, and ESP32. The system detects hand gestures and sends serial commands to ESP32 to control three LEDs.

## 🚀 Features
- **Real-time hand gesture recognition** using MediaPipe.
- **Serial communication** with ESP32.
- **Control three LEDs** based on hand gestures.
- **Interactive and responsive system.**

## 📂 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Vidhyadhar75/Gesture-Lights-ESP32.git
   cd Gesture-Lights-ESP32
   ```
2. Install dependencies:
   ```bash
   pip install opencv-python mediapipe pyserial
   ```

## 🛠 Usage

1. Connect your ESP32 to your computer.
2. Upload the provided ESP32 code to the board.
3. Run the Python script:
   ```bash
   python gesture_lights.py
   ```

## 📊 How It Works
- Captures video from the webcam.
- Uses **MediaPipe Hands** to detect gestures.
- Maps hand gestures to **ON/OFF commands** for LEDs.
- Sends commands to ESP32 **via serial communication**.
- ESP32 receives commands and controls **three LEDs** accordingly.

## ⚡ Serial Commands
- **Gesture 1 → LED 1 ON/OFF**
- **Gesture 2 → LED 2 ON/OFF**
- **Gesture 3 → LED 3 ON/OFF**

## 🤖 Technologies Used
- OpenCV
- MediaPipe
- PySerial
- ESP32 (Arduino IDE)
- Python

## 📌 Contribution
Pull requests are welcome! Improve gesture accuracy or add more features.

![Screenshot 2025-03-27 153828](https://github.com/user-attachments/assets/f3293243-c92f-4b18-89ca-032d22e63376)

