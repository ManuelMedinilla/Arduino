int ledPin = 13; // Pin del LED

void setup() {
  pinMode(ledPin, OUTPUT); // Configura el pin del LED como salida
  Serial.begin(9600); // Inicia la comunicación serie a 9600 baudios
}

void loop() {
  if (Serial.available() > 0) { // Si hay datos disponibles en el puerto serie
    char opcion = Serial.read(); // Lee el dato recibido
    
    if (opcion == '1') {
      digitalWrite(ledPin, HIGH); // Enciende el LED
      Serial.println("LED encendido.");
    } else if (opcion == '0') {
      digitalWrite(ledPin, LOW); // Apaga el LED
      Serial.println("LED apagado.");
    }
  }
}

