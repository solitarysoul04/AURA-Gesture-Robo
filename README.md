<img width="610" height="447" alt="image" src="https://github.com/user-attachments/assets/614c95ad-f088-43ab-b502-9310dd4aae3c" />


# AURA (Autonomous & Unmanned Reconnaissance Agent) 🚙

AURA is an autonomous vehicle that uses a camera to see and hand gestures as an interface to a computer vision system connected via webcam of the computer before which I am sitting to replace the use of a joystick. This project was built with the input of Hack Club.

## 🌟 Key Features
- Dual-Hand Control: Left hand pinch to proportional throttle and right hand gestures to steering using OpenCV and MediaPipe.
- Dual-Band Architecture: High-bandwidth FPV Wi-Fi video transmission (on ESP32-CAM) and Zero-Latency Motor Controls (2.4GHz RF on nRF24L01).
- Two HC-SR04 ultrasonic sensors: with autonomous safety braking on the rover. If an obstacle comes in between the 15cm the rover will automatically stop and will not accept wireless commands.

## 🛒 BoM 
| Category | Product Name | SKU | Qty | Price/Unit (INR) | Link |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Electronics | RF Nano Integrated NRF24L01 Wireless Module | 1121399 | 2 | 1159 | [Buy](https://robu.in/?s=1121399&post_type=product) |
| Electronics | Nano CH340 Chip Board Without USB Cable | 16906 | 2 | 195 | [Buy](https://robu.in/?s=16906&post_type=product) |
| Electronics | ESP32-CAM WiFi + Bluetooth Module | R262524 | 1 | 709 | [Buy](https://robu.in/?s=R262524&post_type=product) |
| Electronics | L298N Dual H Bridge Motor Driver | 51971 | 1 | 176 | [Buy](https://robu.in/?s=51971&post_type=product) |
| Electronics | HC-SR04 Ultrasonic Range Finder Sensor | 2444 | 1 | 65 | [Buy](https://robu.in/?s=2444&post_type=product) |
| Power | Pro-Range INR 18650 11.1V 2000mAh 3S1P Li-Ion Battery | 1237659 | 1 | 899 | [Buy](https://robu.in/?s=1237659&post_type=product) |
| Power | LM2596S DC-DC Buck Converter Power Supply | 11548 | 1 | 42 | [Buy](https://robu.in/?s=11548&post_type=product) |
| Power | Battery Charger 3S Li-ion 12.6V 5A | 1158326 | 1 | 1773 | [Buy](https://robu.in/?s=1158326&post_type=product) |
| Hardware | EasyMech Warrior Chassis for Robotics | 43327 | 1 | 1386 | [Buy](https://robu.in/?s=43327&post_type=product) |
| Hardware | Pro-Range 12V 300 RPM Johnson Geared DC Motor | 5728 | 4 | 540 | [Buy](https://robu.in/?s=5728&post_type=product) |
| Hardware | 85mm Large Robot Smart Car Wheel 38mm Wide | 31509 | 4 | 209 | [Buy](https://robu.in/?s=31509&post_type=product) |
| Hardware | 6mm Hex Motor Coupling 30mm Length | 42874 | 4 | 81 | [Buy](https://robu.in/?s=42874&post_type=product) |
| Cabling | Male to Male Jumper Wires 40Pcs 20cm | 7447 | 1 | 46 | [Buy](https://robu.in/?s=7447&post_type=product) |
| Cabling | 10 Wire Male to Female Jumper Wires 20cm | R160077 | 4 | 14 | [Buy](https://robu.in/?s=R160077&post_type=product) |
| Cabling | 22AWG High Quality Ultra Flexible Silicone Wire - Black | 1824995 | 1 | 18 | [Buy](https://robu.in/?s=1824995&post_type=product) |
| Cabling | 22AWG Single Core Teflon Wire - Red | R257340 | 1 | 24 | [Buy](https://robu.in/?s=R257340&post_type=product) |
| Cabling | Female to Female DuPont Line 40 Pin 30cm | 31321 | 1 | 61 | [Buy](https://robu.in/?s=31321&post_type=product) |
| Cabling | Arduino Nano USB A-Mini B 1.2m Cable | 17844 | 1 | 44 | [Buy](https://robu.in/?s=17844&post_type=product) |
| Cabling | USB TO UART TTL 5V 3.3V FT232RL Adapter | 9707 | 1 | 89 | [Buy](https://robu.in/?s=9707&post_type=product) |
| Consumables | Nylon Cable Zip Ties 150mm White (Pack of 100) | 18279 | 1 | 78 | [Buy](https://robu.in/?s=18279&post_type=product) |
| Consumables | Nylon Cable Zip Ties 300mm White (Pack of 100) | 18280 | 1 | 109 | [Buy](https://robu.in/?s=18280&post_type=product) |
| Consumables | Heat Shrink sleeve 20mm Black | R150615 | 1 | 74 | [Buy](https://robu.in/?s=R150615&post_type=product) |
| Consumables | All Purpose Hot Melt Glue Sticks - 5pcs | 6005 | 1 | 79 | [Buy](https://robu.in/?s=6005&post_type=product) |
| Consumables | Noel Solder Wire 60/40 1.00mm 50gm | 720480 | 1 | 299 | [Buy](https://robu.in/?s=720480&post_type=product) |
| Consumables | Noel FLUX soldering paste-10g | 762465 | 1 | 25 | [Buy](https://robu.in/?s=762465&post_type=product) |
| Prototyping | GL-12 840 Points Solderless Breadboard | 24441 | 1 | 59 | [Buy](https://robu.in/?s=24441&post_type=product) |
| Tools | Screwdriver Set 52 in 1 | 972456 | 1 | 800 | [Buy](https://robu.in/?s=972456&post_type=product) |
| Tools | Soldron 50W 230V Soldering Iron | 143296 | 1 | 699 | [Buy](https://robu.in/?s=143296&post_type=product) |
| Tools | TE-801 LED Magnifier PCB Soldering Stand | 17940 | 1 | 441 | [Buy](https://robu.in/?s=17940&post_type=product) |
| Tools | Multitec 02DX Self Adjusting Wire Cutter - Stripper | 617869 | 1 | 256 | [Buy](https://robu.in/?s=617869&post_type=product) |
| Tools | HTC DM-830L Digital Pocket Multimeter | 775689 | 1 | 649 | [Buy](https://robu.in/?s=775689&post_type=product) |
| Tools | Standard Temp 60Watt Hot Melt Glue Gun | 5998 | 1 | 251 | [Buy](https://robu.in/?s=5998&post_type=product) |
| Tools | Stanley Black+DECKER KR5010V Hammer Drill | R111278 | 1 | 2369 | [Buy](https://robu.in/?s=R111278&post_type=product) |

## 📐 3D CAD Model
This build was done natively in Onshape, with the structural layout and stacking of components. 
**[Link to Onshape Public 3D Model](https://cad.onshape.com/documents/1ed37dd0b596b430698f5eb2/w/aa1a3a995dd5a0a3a9e055b1/e/f5aa9d2bf4de66af82fadf2e?renderMode=0&uiState=6a70e69f9e1a484049917df2)**

## 🛠️ Assembly Instructions

Once I have the required hardware parts I will put the parts together and wire the hardware/electronics as follows:

**1. Mechanical**
* Using the screws included in the kit, attach the EasyMech Warrior aluminium chassis.
* Attach 6mm Hex Motor Couplings to each of the four 300 RPM Johnson Geared Motors, and press the grub screws. 
* Install the motors on chassis brackets, fit the 85mm knobby wheels on the hex couplings.

**2. Electronics**
* The electronics will be sandwiched between the chassis decks as I'm not using a custom PCB. 
* The nylon zip ties from the BOM will be used to securely attach the 11.1V Li-Ion battery to the bottom deck.
* The L298N Motor Driver, LM2596 Buck Converter and the Arduino Nanos will be glued to the board using double sided foam tape as required, and hot glue will be used. 
* The ESP32-CAM will be glued to the top deck mounts that I designed in the CAD model as well as the front and rear HC-SR04 ultrasonic sensors are glued to.

**3. Wiring**
* Connect 11.1V battery to the main power connectors on the L298N motor driver. 
* Rip off the battery wires and connect to the LM2596 Buck Converter. 
* Tune the Buck Converter's potentiometer with the multimeter so the output is 100% with no loading attached to the logic boards.
* Use the Mermaid wiring diagram below to connect the 5V power rail to the Arduinos, ESP32-CAM and sensors. 
* Attach the four DC motors to the L298N's OUT1/OUT2 and OUT3/OUT4 blocks.

**4. Firmware**
* Install Arduino IDE. Install the library “RF24” for the radios.
* Connect the base station Arduino Nano to the laptop using the USB cable, and upload the `Base_Station.ino` file.
* Upload the Arduino Nano to the rover, and upload the file called `Rover_Brain.ino`.
* To install the corresponding dependencies for the Python dashboard, open up the laptop terminal and enter the commands: `pip install opencv-python mediapipe pyserial numpy requests`.
* Change the COM port to the PORT your base station Nano is using: and run the script to open the hand tracking GUI.

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
