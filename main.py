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

#Solicitud de nombre


nombre_ingresado = input("Ingrese un nombre existente: ")

#condicionales para verificar si el nombre ingresado existe.
if nombre_ingresado in nombres:
    print("la edad de", nombre_ingresado, "es", edades[nombre_ingresado])
else: 
    print("el nombre ingresado no existe en la lista")
    opcion = input("¿Desea agregarlo? (s/n): ").lower()

    if opcion == "s":
        edad_nueva = int(input("Ingresa la edad: "))
        nombres.append(nombre_ingresado)
        edades[nombre_ingresado] = edad_nueva
        print("Registro existoso.")
    else:
        print("Operación Cancelada.")

input("Presiona ENTER para continuar...")

print("\n-- Nombres ingresados--")
for nombre, edad in edades.items():
    print(f"{nombre}: {edad} años")