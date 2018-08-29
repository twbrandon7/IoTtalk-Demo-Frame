#include "Seeed_BME280.h"
#include "Bridge.h"
#include <Wire.h>

#define LIGHT_SENSOR A1 //光敏電阻
#define MOISTURE A0 //土壤濕度
#define RELAY_1 4
#define RELAY_2 5
#define RELAY_3 6

int readIntFromBridge();

//BME Sensor使用D2和D3
BME280 bme280;

float temperatures = 0;
float atmosphericPressure = 0;
float altitude = 0;
float humidity = 0;
int lightSensor = 0;
int moisture = 0;

int relays[3] = {0};
char D13data[2];

void setup(){
  Serial.begin(9600);
  Bridge.begin();
  if(!bme280.init()) Serial.println("Device error!");
  
  pinMode(LIGHT_SENSOR, INPUT);
  pinMode(MOISTURE, INPUT);
  pinMode(RELAY_1, OUTPUT);
  pinMode(RELAY_2, OUTPUT);
  pinMode(RELAY_3, OUTPUT);
}

void loop(){
  Bridge.get("Reg_done",  D13data, 2);
  digitalWrite(13, atoi(D13data));
  
  //get and print temperatures
  temperatures = bme280.getTemperature();
  atmosphericPressure = bme280.getPressure();
  altitude = bme280.calcAltitude(atmosphericPressure);
  humidity = bme280.getHumidity();
  lightSensor = analogRead(LIGHT_SENSOR);

  Bridge.put("temperatures", String(temperatures));
  Bridge.put("atmosphericPressure", String(atmosphericPressure));
  Bridge.put("altitude", String(altitude));
  Bridge.put("humidity", String(humidity));
  Bridge.put("lightSensor", String(lightSensor));
  Bridge.put("moisture", String(moisture));

  int data = readIntFromBridge("relay1");
  relays[0] = (data > 0)? HIGH : LOW;

  data = readIntFromBridge("relay2");
  relays[1] = (data > 0)? HIGH : LOW;

  data = readIntFromBridge("relay3");
  relays[2] = (data > 0)? HIGH : LOW;
  
  digitalWrite(RELAY_1, relays[0]);
  digitalWrite(RELAY_2, relays[1]);
  digitalWrite(RELAY_3, relays[2]);
  
  delay(1000);
}

int readIntFromBridge(char *df_name) {
  char data[8];
  Bridge.get(df_name, data, 8);
  return atoi(data);
}
