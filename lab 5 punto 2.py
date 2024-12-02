# Punto 2


# 1. Solicitar un número y determinar si es par o impar
numero = int(input("Introduce un número para verificar si es par o impar: "))
if numero % 2 == 0:
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")


# 2. Usar un bucle for para imprimir los cuadrados de una lista de números
numeros = [1, 2, 3, 4, 5]
print("\nLos cuadrados de los números en la lista son:")
for num in numeros:
    print(f"El cuadrado de {num} es {num ** 2}")


# 3. Usar un bucle while para solicitar repetidamente la entrada del usuario hasta que ingrese un número positivo
while True:
    entrada = int(input("\nIntroduce un número positivo (mayor que 0): "))
    if entrada > 0:
        print(f"¡Gracias! Has introducido el número positivo {entrada}.")
        break
    else:
        print("El número ingresado no es positivo. Intenta de nuevo.")