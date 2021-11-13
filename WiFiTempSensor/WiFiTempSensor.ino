
void setup(void) {
  // start serial port
  Serial.begin(9600);
  Serial.println("WiFi Temp Sensor");
  setupDS18B20();
  setupHttpClient();
}

char json[256];

void loop(void) {
  float tempC = readCelciusDS18B20();
  tempCelciusToJson(json, tempC);
  postJsonData(json);
  delay(10000);
}

void tempCelciusToJson(char *json, float t) {
  if (json)
    sprintf(json, "{ \"tempC\": \"%4.2f\" }", t);
}
