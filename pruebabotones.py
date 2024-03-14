import serial
from serial.tools.list_ports import comports
from time import sleep
from tkinter import *

led_pins = [13, 12, 11]  # Pines a los que están conectados los LEDs
estadoLed = [0, 0, 0]    # Estado inicial de los tres LEDs

import serial
from serial.tools.list_ports import comports
from time import sleep
from tkinter import *

estadoLed = [0, 0, 0]  # Estado inicial de los LEDs

def setup():
    global puerto
    puerto = serial.Serial(comports()[0].device, 9600)
    sleep(2)  # Espera a que se establezca la conexión

def draw():
    global estadoLed
    for i in range(3):
        if estadoLed[i] == 0:
            canvas.create_oval(width/2 - 25 + i * 100, height/2 - 25, width/2 + 25 + i * 100, height/2 + 25, fill="red")
        elif estadoLed[i] == 1:
            canvas.create_oval(width/2 - 22.5 + i * 100, height/2 - 22.5, width/2 + 22.5 + i * 100, height/2 + 22.5, fill="#F4FFA5")

def botonPresionado(numero):
    global estadoLed
    estadoLed[numero] = 1 - estadoLed[numero]  # Cambia el estado del LED correspondiente
    enviar_estado_led()  # Llama a la función para enviar el estado de los LEDs por serial

def enviar_estado_led():
    global estadoLed, puerto
    estado_str = ''.join(map(str, estadoLed))  # Convierte la lista de estados de los LEDs a una cadena
    puerto.write(bytes(estado_str, 'utf-8'))  # Envía el estado de los LEDs por serial

# Configuración de la ventana
root = Tk()
width = 400
height = 200
root.geometry(f"{width}x{height}")
canvas = Canvas(root, width=width, height=height)
canvas.pack()

setup()

# Botones
for i in range(3):
    boton = Button(root, text=f"LED {i+1}", command=lambda num=i: botonPresionado(num))
    boton.place(x=50 + i * 100, y=150)

root.mainloop()  # Mantén la aplicación en funcionamiento
