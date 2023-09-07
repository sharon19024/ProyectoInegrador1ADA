# Investigrar cómo leer un caracter del teclado:
#   Si deseas leer un solo carácter desde el teclado en Python, puedes hacerlo utilizando la función input() junto con indexación para obtener el primer carácter ingresado. 

# Escribir un programa que corra un bucle infinito leyendo e imprimiento las teclas y sólo terminará cuando se presione la tecla ↑ indicada como UP

import keyboard

# Función para verificar si se ha presionado la tecla de flecha arriba (↑)
def check_for_up_key():
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN and event.name == "up":
            print("Se presionó la tecla de flecha arriba (↑). Saliendo del bucle.")
            break

# Iniciar el bucle para verificar la tecla de flecha arriba
check_for_up_key()
