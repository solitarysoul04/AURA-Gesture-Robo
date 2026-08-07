<img width="573" height="447" alt="image" src="https://github.com/user-attachments/assets/435f5ecc-cc68-42f7-af40-14ef1d847f9c" />



# AURA (Autonomous & Unmanned Reconnaissance Agent) Rover🚙

AURA Rover is a visionary project which I brainstormed during building for Macondo by HackClub. It is an autonomous project that will use a computer vision interface which will incorporate MediaPipe and OpenCV which will detect and read the hand gestures on-board for hopefully successful movement of the rover. This idea was brainstormed to replace the use of joystick and sit back lazy controlling the rover with just your physical hands assisted by ESP32-CAM feed on your system.

## 🌟 Key Features
- Dual-Hand Control: Pinching fingers of left hand will trigger the throttle and right hand gestures will act as an steering using OpenCV and MediaPipe.
- Dual-Band Architecture: Video will be transmitted via ESP32-CAM high-bandwidth FPV Wi-Fi and for Zero-Latency Motor Controls, 2.4GHz RF on nRF24L01 will be used.
- Two HC-SR04 ultrasonic sensors: Since the rover will be autonomous, for safety and instant braking of the rover, two ultrasonic sensors (one at front and another at back) will keep a watch on obstacles and will avoid any crash by stopping rover if something is detected within 15cm and will not accept the wireless commands.

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
* First step will be to assemble the EasyMech Warrior aluminium chassis using the screws and resources included within the kit.
* Further, I will attach the 6mm Motor Couplings to each of four Johnson Geared Motors and tighten them up.
* Fit the wheels on motors, and install them on chassis along with motors. 

**2. Electronics**
* The L298N Motor Driver, LM2596 Buck Converter and Arduino Nanos will be glued to the base using either double sided foam tape or hot glue as seem necessary.
* ESP32-CAM, HC-SR04 and other necessary components will be glued accordingly to the CAD Model submitted.
* 11.1V Li-ion battery will be tied up with nylon zip to fix it.

**3. Wiring**
* 11.1V battery will be connected to main power connectors on L298N motor driver.
* Battery wires will be stripped off and will be connected to LM2596 Buck Converter.
* All other necessary connections of ESP32-CAM, Arduino, 5V, etc. will be done with reference to below Mermaid wiring diagram.

**4. Firmware**
* For logic processing, we will first install Arduino IDE to program the microcontroller and "RF24" library too for the radios.
* Base station Arduino Nano will be connected to laptop using the USB Cable to upload the `Base_Station.ino` file.
* For rover movement, another Arduino Nano will be updated with the code file `Rover_Brain.ino`.
* For successful working of the scripts, firmwares and GUI, corresponding dependencies need to be installed... This must be done via the terminal by entering command: `pip install opencv-python mediapipe pyserial numpy requests`.
* Finally, COM port need to be changed into the PORT of our base station Arduino Nano and run the script `Mission_Control.py` to open the hand tracking GUI.

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
