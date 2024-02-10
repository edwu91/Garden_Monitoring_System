#include <Adafruit_BME280.h>
#include <Wire.h>         // adds I2C library 
#include <BH1750.h>    


Adafruit_BME280 bme;
BH1750 lightMeter;

const int AirValue = 620;   //you need to replace this value with Value_1
const int WaterValue = 310;  //you need to replace this value with Value_2
int readVal =0;
int soilmoistureVal =0;
float Temp = 0.001;
float Pressure = 0.001;
float Humidity = 0.001;
float LUX = 0.001;

void setup() {
  //Serial.begin(250000);
  Serial.begin(57600);
  if (!bme.begin(0x76)) 
  {
    Serial.println("Could not find a valid BME280 sensor, check wiring!");
    //while (1);
  }
  Wire.begin();
  Wire.setClock(400000);
  lightMeter.begin();
  pinMode(6, OUTPUT);
  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
  digitalWrite(6, HIGH);
  digitalWrite(7, HIGH);
  digitalWrite(8, HIGH);
  digitalWrite(9, HIGH);
}
void loop() {
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n'); //change to readbyteuntil
    if (data =="A"){
      Temp = bme.readTemperature();
      Pressure = bme.readPressure();
      Humidity = bme.readHumidity();
      LUX = lightMeter.readLightLevel();
      String val = String(Temp) + ";" + String(Pressure) + ";" + String(Humidity) + ";" + String(LUX);
      Serial.print(val);
    }
    if (data == "T"){
      float res = bme.readTemperature();
      Serial.print(res);
    }
    if (data == "P"){
      float res = bme.readPressure();
      Serial.print(res);
    }
    if (data=="H"){
      float res = bme.readHumidity();
      Serial.print(res);
    }
    if (data=="L"){
      float lux = lightMeter.readLightLevel();
      Serial.print(lux);
    }
    if (data=="M1"){
      readVal = analogRead(A0); 
      soilmoistureVal = map(readVal, AirValue, WaterValue, 0, 1000);
      Serial.print(soilmoistureVal);
    }
    if (data=="M2"){
      readVal = analogRead(A1); 
      soilmoistureVal = map(readVal, AirValue, WaterValue, 0, 1000);
      Serial.print(soilmoistureVal);
    }
    if (data=="M3"){
      readVal = analogRead(A2); 
      soilmoistureVal = map(readVal, AirValue, WaterValue, 0, 1000);
      Serial.print(soilmoistureVal);
    }
    if (data=="M4"){
      readVal = analogRead(A3); 
      soilmoistureVal = map(readVal, AirValue, WaterValue, 0, 1000);
      Serial.print(soilmoistureVal);
    }
    if (data=="P1ON"){
      digitalWrite(9,LOW);
      Serial.print("P1-ON");}
    if (data=="P1OFF"){
      digitalWrite(9,HIGH);
      Serial.print("P1-OFF");}
    if (data=="P2ON"){
      digitalWrite(8,LOW);
      Serial.print("P2 ON");}
    if (data=="P2OFF"){
      digitalWrite(8,HIGH);
      Serial.print("P2-OFF");}
    if (data=="P3ON"){
      digitalWrite(7,LOW);
      Serial.print("P3-ON");}
    if (data=="P3OFF"){
      digitalWrite(7,HIGH);
      Serial.print("P3-OFF");}
    if (data=="P4ON"){
      digitalWrite(6,LOW);
      Serial.print("P4-ON");}
    if (data=="P4OFF"){
      digitalWrite(6,HIGH);
      Serial.print("P4-OFF");}
  }
}
