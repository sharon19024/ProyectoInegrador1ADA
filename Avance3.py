import os

def limpiar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    numero = 0

    while numero <= 50:
        tecla = input("Presiona 'n' para continuar: ")

        if tecla == 'n':
            limpiar_terminal()
            print(f"Número actual: {numero}")
            numero += 1
        else:
            print("Presiona 'n'")
if __name__ == "__main__":
    main()

