#include<HardwareSerial.h>
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}
int i = 1;
void loop() {
  // put your main code here, to run repeatedly:
  int sensorValue = analogRead(A0);
  Serial.print("Analog value: ");
  Serial.println(sensorValue);
  delay(1000);
}
