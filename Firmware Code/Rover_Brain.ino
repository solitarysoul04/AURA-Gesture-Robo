#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

// Hardware Pins
#define CE_PIN 9
#define CSN_PIN 8

// L298N Motor Driver Pins
#define IN1 2
#define IN2 3
#define IN3 4
#define IN4 6
#define ENA 5 
#define ENB 10

// Front HC-SR04 Pins
#define TRIG_FRONT A0
#define ECHO_FRONT A1

RF24 radio(CE_PIN, CSN_PIN);
const byte address[6] = "00001"; 
const int SAFE_DISTANCE_CM = 15; 

struct Data_Package {
  char direction;
  byte speed;
};
Data_Package data = {'S', 0}; // safe STOP state

void setup() {
  pinMode(IN1, OUTPUT); pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT); pinMode(IN4, OUTPUT);
  pinMode(ENA, OUTPUT); pinMode(ENB, OUTPUT);

  pinMode(TRIG_FRONT, OUTPUT); 
  pinMode(ECHO_FRONT, INPUT);

  radio.begin();
  radio.openReadingPipe(0, address);
  radio.setPALevel(RF24_PA_LOW);
  radio.startListening();
}

void loop() {
  // Front Sensor
  int frontDist = getDistance(TRIG_FRONT, ECHO_FRONT);

  if (radio.available()) {
    radio.read(&data, sizeof(Data_Package));
  }

  if (data.direction == 'F' && frontDist > 0 && frontDist < SAFE_DISTANCE_CM) {
    data.direction = 'S'; 
    data.speed = 0;
  }

  executeMotorCommand(data.direction, data.speed);
}

int getDistance(int trigPin, int echoPin) {
  digitalWrite(trigPin, LOW); delayMicroseconds(2);
  digitalWrite(trigPin, HIGH); delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  
  long duration = pulseIn(echoPin, HIGH, 15000); 
  if (duration == 0) return 999; 
  return duration * 0.034 / 2;
}

void executeMotorCommand(char dir, byte spd) {
  analogWrite(ENA, spd);
  analogWrite(ENB, spd);

  switch (dir) {
    case 'F': digitalWrite(IN1, HIGH); digitalWrite(IN2, LOW); digitalWrite(IN3, HIGH); digitalWrite(IN4, LOW); break;
    case 'B': digitalWrite(IN1, LOW); digitalWrite(IN2, HIGH); digitalWrite(IN3, LOW); digitalWrite(IN4, HIGH); break;
    case 'L': digitalWrite(IN1, LOW); digitalWrite(IN2, HIGH); digitalWrite(IN3, HIGH); digitalWrite(IN4, LOW); break;
    case 'R': digitalWrite(IN1, HIGH); digitalWrite(IN2, LOW); digitalWrite(IN3, LOW); digitalWrite(IN4, HIGH); break;
    case 'S': default: digitalWrite(IN1, LOW); digitalWrite(IN2, LOW); digitalWrite(IN3, LOW); digitalWrite(IN4, LOW); break;
  }
}
