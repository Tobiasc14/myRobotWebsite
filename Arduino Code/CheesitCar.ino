#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>
#include <printf.h>

const int directionA1 = 7;
const int PWMA = 6;
const int directionA2 = 5;

const int directionB1 = 4;
const int PWMB = 3;
const int directionB2 = 2;

RF24 radio(8,9);
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  radio.begin();
  radio.openReadingPipe(1, 0xE8E8F0F0E1LL);
  radio.setChannel(0x77);
  radio.setPALevel(RF24_PA_MIN);
  radio.enableDynamicPayloads();
  radio.setPayloadSize(32);
  radio.setAutoAck(false);
  radio.enableAckPayload();
  radio.printDetails();
  radio.startListening();
  Serial.println("Reciever is set up"); 

  pinMode(directionA1, OUTPUT);
  pinMode(directionA2, OUTPUT);
  pinMode(PWMA, OUTPUT);
  pinMode(directionB1, OUTPUT);
  pinMode(directionB2, OUTPUT);
  pinMode(PWMB, OUTPUT);
  Serial.println("Car is set up"); 

}

void loop() {
  // put your main code here, to run repeatedly:
  if (!(radio.available(0))){
    delay(50);
    //Serial.println("Nothing yet");
  }
  else{
    char receivedMessage[32] = {0} ;   // set incmng message for 32 bytes
    radio.read(receivedMessage, sizeof(receivedMessage));
    String message = String(receivedMessage[0]);
    
    if (message.equals("s")){
      stopCar();
    }
    else if (message.equals("f")){
      forward(250);
    }
    else if (message.equals("b")){
      backward(250);
    }
    else if (message.equals("l")){
      left(250);
    }
    else if (message.equals("r")){
      right(250);
    }
    else{
      stopCar();
    }
    Serial.println(message);
    //radio.flush_rx();
  }

}
void stopCar(){
 digitalWrite(directionA1, LOW);
 digitalWrite(directionA2, LOW);
 analogWrite(PWMA, 0);
 digitalWrite(directionB1, LOW);
 digitalWrite(directionB2, LOW);
 analogWrite(PWMB, 0);
}
void forward(int speed){
 digitalWrite(directionA1, LOW);
 digitalWrite(directionA2, HIGH);
 analogWrite(PWMA, speed);
 digitalWrite(directionB1, LOW);
 digitalWrite(directionB2, HIGH);
 analogWrite(PWMB, speed);
}
void backward(int speed){
 digitalWrite(directionA1, HIGH);
 digitalWrite(directionA2, LOW);
 analogWrite(PWMA, speed);
 digitalWrite(directionB1, HIGH);
 digitalWrite(directionB2, LOW);
 analogWrite(PWMB, speed);
}
void left(int speed){
 digitalWrite(directionA1, HIGH);
 digitalWrite(directionA2, LOW);
 analogWrite(PWMA, speed);
 digitalWrite(directionB1, LOW);
 digitalWrite(directionB2, HIGH);
 analogWrite(PWMB, speed);
}
void right(int speed){
 digitalWrite(directionA1, LOW);
 digitalWrite(directionA2, HIGH);
 analogWrite(PWMA, speed);
 digitalWrite(directionB1, HIGH);
 digitalWrite(directionB2, LOW);
 analogWrite(PWMB, speed);
}
