import random

def juego_adivinanza():
    print("Bienvenido al juego de adivinanza")

    numero_aleatorio = random.randint(1, 100)
    intentos = 0
    while True:
        try:
            adivinanza = int(input("Adivina el número (entre 1 y 100): "))
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue
        intentos += 1
        
        if adivinanza < numero_aleatorio:
            print("El número es mayor.")
        elif adivinanza > numero_aleatorio:
            print("El número es menor.")
        else:
            print(f"¡Felicidades! Has adivinado el número {numero_aleatorio} en {intentos} intentos.")
            break
juego_adivinanza()
