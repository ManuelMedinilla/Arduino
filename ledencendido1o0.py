import serial
import time

# Establece el puerto serie y la velocidad de comunicación
puerto_serie = serial.Serial('COM4', 9600)  
time.sleep(2)  # Espera a que se establezca la conexión

try:
    while True:
        opcion = input("Ingrese 1 para encender el LED o 0 para apagarlo: ")
        if opcion == '1' or opcion == '0':
            puerto_serie.write(opcion.encode())  # Envía la opción al Arduino
        else:
            print("Opción no válida. Ingrese 1 o 0.")
except KeyboardInterrupt:
    puerto_serie.close()  # Cierra el puerto serie cuando se interrumpe el programa
