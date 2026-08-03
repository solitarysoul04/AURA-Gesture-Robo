<img width="610" height="447" alt="image" src="https://github.com/user-attachments/assets/614c95ad-f088-43ab-b502-9310dd4aae3c" />

*> Banner: Onshape CAD Rendering of the AURA Rover (Hardware Build Pending)*

# AURA (Autonomous & Unmanned Reconnaissance Agent) 🚙

AURA is an autonomous underwater vehicle that uses hand gestures as an interface to a computer vision system to replace the use of a joystick. This project was built with the input of Hack Club.

## 🌟 Key Features
- Dual-Hand Control: Left hand pinch to proportional throttle and right hand gestures to steering using OpenCV and MediaPipe.
- Dual-Band Architecture: High-bandwidth FPV Wi-Fi video transmission (on ESP32-CAM) and Zero-Latency Motor Controls (2.4GHz RF on nRF24L01).
- Two HC-SR04 ultrasonic sensors: with autonomous safety braking on the rover. If an obstacle comes in between the 15cm the rover will automatically stop and will not accept wireless commands.

## 📐 3D CAD Model
This build was done natively in Onshape, with the structural layout and stacking of components. 
**[Link to Onshape Public 3D Model](https://cad.onshape.com/documents/1ed37dd0b596b430698f5eb2/w/aa1a3a995dd5a0a3a9e055b1/e/f5aa9d2bf4de66af82fadf2e?renderMode=0&uiState=6a70e69f9e1a484049917df2)**

## 🔌 Hardware Wiring Diagram

```mermaid
graph TD
    %% Power Distribution
    BAT([11.1V Li-Ion Battery]) ==>|11.1V Power| L298N[L298N Motor Driver]
    BAT ==>|11.1V Power| BUCK[LM2596 Buck Converter]
    BUCK ==>|Steps down to 5V| 5V_RAIL((5V Logic Rail))

    %% 5V Connections
    5V_RAIL -->|VIN| NANO[RF Nano Integrated]
    5V_RAIL -->|5V Pin| ESP[ESP32-CAM]
    5V_RAIL -->|VCC| HC1[Front HC-SR04]
    
    %% Common Ground
    GND_RAIL((Common GND)) --- BAT
    GND_RAIL --- BUCK
    GND_RAIL --- L298N
    GND_RAIL --- NANO
    GND_RAIL --- ESP
    GND_RAIL --- HC1

    %% Data Connections
    NANO -.->|D5, D10| L298N_PWM(L298N ENA/ENB)
    NANO -.->|D2, D3, D4, D6| L298N_DIR(L298N IN1-IN4)
    NANO -.->|A0, A1| HC1_DATA(HC-SR04 Trig/Echo)

    %% Motor Outputs
    L298N ===>|OUT1, OUT2| ML((Left Gear Motors))
    L298N ===>|OUT3, OUT4| MR((Right Gear Motors))
