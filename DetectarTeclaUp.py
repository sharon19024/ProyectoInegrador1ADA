# Investigrar cómo leer un caracter del teclado:
#   Si deseas leer un solo carácter desde el teclado en Python, puedes hacerlo utilizando la función input() junto con indexación para obtener el primer carácter ingresado. 

# Escribir un programa que corra un bucle infinito leyendo e imprimiento las teclas y sólo terminará cuando se presione la tecla ↑ indicada como UP

import readchar

# Función para verificar si se ha presionado la tecla de flecha arriba (↑)
def check_for_up_key():
    while True:
        char = readchar.readkey()
        if ord(char[0]) == 27:  # Código ASCII para el carácter de escape (ESC)
            char = readchar.readkey()
            if ord(char[0]) == 91:  # Código ASCII para '['
                char = readchar.readkey()
                if ord(char[0]) == 65:  # Código ASCII para 'A'
                    print("Se presionó la tecla de flecha arriba (↑). Saliendo del bucle.")
                    break

# Iniciar el bucle para verificar la tecla de flecha arriba
check_for_up_key()
