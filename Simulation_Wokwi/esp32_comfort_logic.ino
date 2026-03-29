#include "model_data.h"
#include "DHT.h"

// Pin Definitions for 30-pin ESP32
#define DHTPIN 15   
#define POTPIN 34    
#define DHTTYPE DHT22

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(115200);
  dht.begin();
  Serial.println("--- Smart Campus AI Monitor ---");
  Serial.println("System Initialized...");
}

void loop() {
  // 1. Read the virtual sensors
  float t = dht.readTemperature();
  float h = dht.readHumidity();
  int rawGas = analogRead(POTPIN);

  float scaledTemp = (t - (-10.0)) / (45.0 - (-10.0));
  float scaledGas = (rawGas / 4095.0); // Potentiometer is 0 to 4095

  // Output the readings
  Serial.print("Temp: "); Serial.print(t);
  Serial.print("C | Raw Gas: "); Serial.print(rawGas);

  // The Decision Logic
  if(rawGas > 2000 || t > 30) {
    Serial.println(" -> Result: POOR QUALITY");
  } else {
    Serial.println(" -> Result: GOOD QUALITY");
  }
  
  delay(2000); 
}