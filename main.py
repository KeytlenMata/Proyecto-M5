# Mensaje de bienvenida centrado
ancho = 70
print("=" * ancho)
print("¡Bienvenido al Sistema de Consulta de Edades!".center(ancho))
print("=" * ancho)
print("Introduce un nombre que forme parte del sistema.")
print("-" * ancho)

# Lista de nombres 
nombres = ["Lucas", "Ana", "John", "Mia", "Felix"]

# Diccionario de edades 
edades = {
    "Lucas": 22,
    "Ana": 21,
    "John": 23,
    "Mia": 20,
    "Felix": 24,
}

# Bucle principal
while True:
    # Solicitar un nombre
    nombre_ingresado = input("\nIngrese un nombre: ").strip()

    # Cláusula para búsqueda sin distinción de mayúsculas/minúsculas
    nombre_encontrado = None
    for nombre in edades:
        if nombre.lower() == nombre_ingresado.lower():
            nombre_encontrado = nombre
            break

    if nombre_encontrado:
        print(f"\n{nombre_encontrado} tiene {edades[nombre_encontrado]} años.")
    else:
        print("El nombre ingresado no existe en el sistema.")
        opcion = input("¿Desea agregarlo? (s/n): ").lower().strip()
        if opcion == "s":
            try:
                edad_nueva = int(input("Ingresa la edad: "))
                nombres.append(nombre_ingresado)
                edades[nombre_ingresado] = edad_nueva
                print("Registro exitoso.")
            except ValueError:
                print("Edad inválida. No se agregó el registro.")
        else:
            print("Operación cancelada.")

    # Preguntar qué hacer a continuación
    print("\n¿Qué deseas hacer ahora?")
    print("a) Introducir otro nombre")
    print("b) Ver la lista de nombres ingresados")
    print("c) Salir del sistema")
    
    siguiente = input("Elige una opción (a/b/c): ").lower().strip()
    
    if siguiente == "b":
        print("\n-- Nombres ingresados --")
        for nombre, edad in edades.items():
            print(f"{nombre}: {edad} años")
        print("\n¿Qué deseas hacer ahora?")
        print("a) Introducir otro nombre")
        print("c) Salir del sistema")
        siguiente = input("Elige una opción (a/c): ").lower().strip()

    if siguiente == "c":
        print("\nGracias por usar el sistema. ¡Hasta pronto!")
        break