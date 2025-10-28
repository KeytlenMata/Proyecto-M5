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