#define LED_PIN 13

void setup() {
  pinMode(LED_PIN, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available()) {
    char command = Serial.read();
    switch (command) {
      case 'H':
        digitalWrite(LED_PIN, HIGH);
        break;
      case 'L':
        digitalWrite(LED_PIN, LOW);
        break;
    }
  }
}



// the above script was automatically generated using the github ai copilot tool. it merely saves as a translation layer so the python script works with the arduino uno board since we were having problems with the pyfirmata library -ABQ