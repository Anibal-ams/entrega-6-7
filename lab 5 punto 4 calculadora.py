def calculadora():
    print("Bienvenido a la calculadora básica")
    
    while True:
        print("\nOperaciones disponibles:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")
        operacion = input("Elige una operación (1/2/3/4/5): ")
        if operacion == '5':
            print("¡Gracias por usar la calculadora!")
            break

        try:
            num1 = float(input("Introduce el primer número: "))
            num2 = float(input("Introduce el segundo número: "))
        except ValueError:
            print("Por favor, ingresa números válidos.")
            continue

        if operacion == '1':
            resultado = num1 + num2
            print(f"El resultado de la suma es: {resultado}")
        elif operacion == '2':
            resultado = num1 - num2
            print(f"El resultado de la resta es: {resultado}")
        elif operacion == '3':
            resultado = num1 * num2
            print(f"El resultado de la multiplicación es: {resultado}")
        elif operacion == '4':
            if num2 != 0:
                resultado = num1 / num2
                print(f"El resultado de la división es: {resultado}")
            else:
                print("Error: No se puede dividir entre cero.")
        else:
            print("Opción no válida. Por favor, elige una operación válida.")
calculadora()
