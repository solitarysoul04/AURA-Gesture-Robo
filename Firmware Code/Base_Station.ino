#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

// NRF24 module
RF24 radio(9, 8); 
const byte address[6] = "00001";

// RF transmission
struct Data_Package {
  char direction;
  byte speed;
};
Data_Package data;

void setup() {
  Serial.begin(115200); 
  
  if (!radio.begin()) { 
    while (1);
  }
  
  radio.openWritingPipe(address);
  radio.setPALevel(RF24_PA_LOW);
  radio.stopListening();
  
  // STOP state
  data.direction = 'S';
  data.speed = 0;
}

void loop() {
  if (Serial.available() > 0) {
    String input = Serial.readStringUntil('\n');
    int commaIndex = input.indexOf(',');
    
    if (commaIndex > 0) {
      data.direction = input.charAt(0);
      data.speed = input.substring(commaIndex + 1).toInt();
      radio.write(&data, sizeof(Data_Package));
    }
  }
}
