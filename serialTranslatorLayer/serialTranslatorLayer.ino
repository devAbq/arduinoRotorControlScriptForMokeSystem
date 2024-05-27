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