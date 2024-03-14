void setup() {
  pinMode(13, OUTPUT);
  Serial.begin(9600); // Inicia la comunicación serial
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read(); // Lee el comando enviado por Python
    if (command == 'H') {
      digitalWrite(13, HIGH); // Enciende el LED
    } else if (command == 'L') {
      digitalWrite(13, LOW);  // Apaga el LED
    }
  }
}