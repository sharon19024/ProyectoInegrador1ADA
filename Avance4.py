import os
from typing import List, Tuple

# Convertir el laberinto de una cadena a una matriz
def convertir_a_matriz(laberinto_str: str) -> List[List[str]]:
    lineas = laberinto_str.split("\n")
    laberinto = [list(linea) for linea in lineas]
    return laberinto

# Mostrar el laberinto
def mostrar_laberinto(laberinto: List[List[str]]):
    for fila in laberinto:
        print("".join(fila))

# limpiar la pantalla
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')


def main_loop(laberinto: List[List[str]], pos_inicial: Tuple[int, int], pos_final: Tuple[int, int]):
    px, py = pos_inicial

    while (px, py) != pos_final:
        laberinto[px][py] = 'P'  
        limpiar_pantalla()
        mostrar_laberinto(laberinto)
        laberinto[px][py] = '.'  

        # Leer la entrada del teclado
        tecla = input("Presiona una tecla (↑ ↓ ← →) para mover al jugador: ")

        # Actualizar la posición del jugador si es válida
        if tecla == '↑' and px > 0 and laberinto[px - 1][py] != '#':
            px -= 1
        elif tecla == '↓' and px < len(laberinto) - 1 and laberinto[px + 1][py] != '#':
            px += 1
        elif tecla == '←' and py > 0 and laberinto[px][py - 1] != '#':
            py -= 1
        elif tecla == '→' and py < len(laberinto[0]) - 1 and laberinto[px][py + 1] != '#':
            py += 1

# El laberinto en forma de cadena
laberinto_str = '''\
..###################
....#.....#...#.....#
#.#.#.#.###.###.#.###
#.#.#.#.#...#...#.#.#
#.#####.#.#.###.###.#
#...#.....#...#.....#
#.###.#.#####.#.#.###
#.....#.#.......#.#.#
#.#.#.#####.#.#.#.#.#
#.#.#.....#.#.#.#...#
#.#######.###.###.#.#
#...#.#.#.#.....#.#.#
###.#.#.###.###.#.#.#
#...#.....#.#...#.#.#
#.###.#############.#
#.......#.#.#...#...#
#.#.#####.#.###.###.#
#.#...#.#...........#
#.###.#.#.###.#.#####
#.#.....#.#...#.....#
###################.#
'''

# Definir las posiciones inicial y final
posicion_inicial = (0, 0)
posicion_final = (len(laberinto_str.split("\n")) - 1, len(laberinto_str.split("\n")[0]) - 1)

# Convertir la cadena de laberinto a una matriz
laberinto = convertir_a_matriz(laberinto_str)

# Ejecutar el bucle principal del juego
main_loop(laberinto, posicion_inicial, posicion_final)

