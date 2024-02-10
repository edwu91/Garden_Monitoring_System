#include <Adafruit_BME280.h>
    


Adafruit_BME280 bme;


void setup() {
  Serial.begin(9600);
  if (!bme.begin(0x76)) 
  {
    Serial.println("Could not find a valid BME280 sensor, check wiring!");
    while (1);
  }
}
void loop() {
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');
    if (data == "T"){
      Serial.print(bme.readTemperature());
    }
    if (data == "P"){
      Serial.print(bme.readPressure());
    }
    if (data=="H"){
      Serial.print(bme.readHumidity());
    }

  }
}
