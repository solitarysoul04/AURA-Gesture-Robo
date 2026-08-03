# AURA (Autonomous & Unmanned Reconnaissance Agent) 🚙

AURA is an autonomous underwater vehicle that uses hand gestures as an interface to a computer vision system to replace the use of a joystick. This project was built with the input of Hack Club.

## 🌟 Key Features
- Dual-Hand Control: Left hand pinch to proportional throttle and right hand gestures to steering using OpenCV and MediaPipe.
- Dual-Band Architecture: High-bandwidth FPV Wi-Fi video transmission (on ESP32-CAM) and Zero-Latency Motor Controls (2.4GHz RF on nRF24L01).
- Two HC-SR04 ultrasonic sensors: with autonomous safety braking on the rover. If an obstacle comes in between the 15cm the rover will automatically stop and will not accept wireless commands.

## 📐 3D CAD Model
This build was done natively in Onshape, with the structural layout and stacking of components. 
**[Link to Onshape Public 3D Model](https://cad.onshape.com/documents/1ed37dd0b596b430698f5eb2/w/aa1a3a995dd5a0a3a9e055b1/e/f5aa9d2bf4de66af82fadf2e?renderMode=0&uiState=6a70e69f9e1a484049917df2)**
