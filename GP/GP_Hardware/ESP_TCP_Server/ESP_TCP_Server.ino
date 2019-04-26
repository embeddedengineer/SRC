#include "ESP8266WiFi.h"  
const int port = 8010;
const char* ssid = "Abdo Adsl";
const char* password =  "arduinoabdo";
 
WiFiServer wifiServer(port);
 
void setup() {
 
  Serial.begin(115200);
 
  delay(1000);
  WiFi.begin(ssid, password);
 
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
  }
 
  wifiServer.begin();
}
 
void loop() {
 
  WiFiClient client = wifiServer.available();

  if (Serial.available() > 0) {
    String Command = Serial.readString();
    if (Command == "IP") Serial.println(WiFi.localIP());
    else if (  Command == "PORT" ) Serial.println(port);
  }
  
  else if (client) {
 
    while (client.connected()) {
      if (client.available() > 0) {
        Serial.println(client.readString());
      }
      else if (Serial.available() > 0) {
        client.println(Serial.readString());
      }
      delay(10);
    }
    
    client.stop();
  }

  
  
}

