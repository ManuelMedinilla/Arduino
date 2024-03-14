int ledPines[] = {13, 12, 11}; // Pines para los LEDs

void setup() {
  Serial.begin(9600);  // Inicia la comunicación serial a 9600 baudios
  for (int i = 0; i < 3; i++) {
    pinMode(ledPines[i], OUTPUT); // Configura los pines de los LEDs como salida
  }
}

void loop() {
  if (Serial.available() >= 3) { // Si hay al menos tres bytes disponibles para leer
    String estado = Serial.readString(); // Lee el estado de los LEDs enviado desde Python
    for (int i = 0; i < 3; i++) {
      if (estado.charAt(i) == '0') {
        digitalWrite(ledPines[i], LOW); // Apaga el LED correspondiente
      } else if (estado.charAt(i) == '1') {
        digitalWrite(ledPines[i], HIGH); // Enciende el LED correspondiente
      }
    }
  }
}
