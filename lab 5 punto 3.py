#punto3


# 1. Crear una lista de nombres de estudiantes y mostrar cada uno utilizando un bucle
estudiantes = ["Juan", "Ana", "Pedro", "María", "Luis"]
print("Lista de estudiantes:")
for estudiante in estudiantes:
    print(estudiante)

# 2. Crear un diccionario simple con información de contacto y mostrar sus claves y valores
contactos = {
    "Juan": "juan@email.com",
    "Ana": "ana@email.com",
    "Pedro": "pedro@email.com"
}

print("\nInformación de contacto:")
for nombre, correo in contactos.items():
    print(f"Nombre: {nombre}, Correo: {correo}")

# 3. Implementar un script para que el usuario agregue elementos a la lista o actualice valores en el diccionario
while True:
    print("\n¿Qué te gustaría hacer?")
    print("1. Agregar un estudiante a la lista.")
    print("2. Actualizar un correo en el diccionario.")
    print("3. Salir.")
    opcion = input("Selecciona una opción (1, 2 o 3): ")

    if opcion == '1':
        nuevo_estudiante = input("Introduce el nombre del nuevo estudiante: ")
        estudiantes.append(nuevo_estudiante)
        print(f"Estudiante {nuevo_estudiante} agregado a la lista.")

    elif opcion == '2':
        nombre = input("Introduce el nombre del estudiante para actualizar su correo: ")
        if nombre in contactos:
            nuevo_correo = input(f"Introduce el nuevo correo para {nombre}: ")
            contactos[nombre] = nuevo_correo
            print(f"Correo de {nombre} actualizado.")
        else:
            print(f"El estudiante {nombre} no está en el diccionario.")

    elif opcion == '3':
        print("¡Hasta luego!")
        break

    else:
        print("Opción no válida. Intenta de nuevo.")