import serial
import time

# Conecta al puerto serie del Arduino
arduino = serial.Serial('COM4', 9600)  # Asegúrate de ajustar el nombre del puerto COM

# Espera a que se establezca la conexión
time.sleep(2)

# Parpadea el LED 5 veces
for _ in range(5):
    arduino.write(b'H')  # Enciende el LED
    time.sleep(1)        # Espera 1 segundo
    arduino.write(b'L')  # Apaga el LED
    time.sleep(1)        # Espera 1 segundo

# Deja el LED encendido durante 10 segundos
arduino.write(b'H')      # Enciende el LED
time.sleep(10)           # Espera 10 segundos

# Apaga el LED al finalizar
arduino.write(b'L')      # Apaga el LED

# Cierra la conexión
arduino.close()