"""
Día 5 - Diccionarios (Dictionaries)
Autor: Ignacio Quijada
Fecha: 2026-03-07
Descripción:
Ejercicios de Python enfocados en el uso de diccionarios.
Se practican creación, acceso a valores, iteración y operaciones básicas.
"""

# -----------------------------------
# Ejercicio 1
# Crea un diccionario con información de una persona:
# nombre, edad y ciudad.
# Luego imprime el diccionario completo.
# -----------------------------------

print("Ejercicio 1:")

person={"Name":"Ignacio"
    ,"Age":28
    ,"City":"Santiago"}
print(person)

# -----------------------------------
# Ejercicio 2
# Usando el diccionario del ejercicio anterior,
# imprime solo el valor de "nombre".
# -----------------------------------

print("Ejercicio 2:")

print(person["Name"])


# -----------------------------------
# Ejercicio 3
# Agrega una nueva clave "profesion" al diccionario
# con el valor que quieras.
# Luego imprime el diccionario actualizado.
# -----------------------------------

print("Ejercicio 3:")

person["Profession"]="Scientist"
print(person)


# -----------------------------------
# Ejercicio 4
# Crea un diccionario con 3 frutas como claves
# y sus precios como valores.
# Imprime el precio de una de ellas.
# -----------------------------------

print("Ejercicio 4:")

fruits={"Mango":150,"Apple":50,"Banana":100}
print(fruits["Banana"])


# -----------------------------------
# Ejercicio 5
# Recorre el diccionario de frutas con un bucle
# e imprime cada clave.
# -----------------------------------

print("Ejercicio 5:")

for fruit in fruits:
    print(fruit)

# -----------------------------------
# Ejercicio 6
# Recorre el diccionario e imprime:
# fruta y precio.
# Ejemplo:
# manzana -> 500
# -----------------------------------

print("Ejercicio 6:")

for fruit in fruits:
    print(f"{fruit} -> {fruits[fruit]}")


# -----------------------------------
# Ejercicio 7
# Pide al usuario un nombre.
# Si el nombre existe en un diccionario de estudiantes,
# imprime su nota.
# Si no existe, imprime "Estudiante no encontrado".
# -----------------------------------

print("Ejercicio 7:")

names={"Juan":5.5,"Josh":4.3,"Peter":6.6,"Alfred":2.1}
student=input("Introduce un nombre: ").capitalize()
if student in names:
    print(f"La nota de {student} es: {names[student]}.")
else:
    print("Estudiante no encontrado.")

# -----------------------------------
# Ejercicio 8
# Dado un diccionario con nombres y edades,
# imprime solo las personas mayores de 18 años.
# -----------------------------------

print("Ejercicio 8:")

ages_dict={"Diego":22,"Ana":21,"Sofía":11,"Carlos":9,"Max":33}
for key,value in ages_dict.items():
    if value > 18:
        print(f"{key} -> {value}")

# -----------------------------------
# Ejercicio 9
# Cuenta cuántas veces aparece cada palabra
# en una frase ingresada por el usuario.
# Pista:
# usa split() y un diccionario.
# -----------------------------------

print("Ejercicio 9:")
frase="Hola a todos los estudiantes presentes en este lugar. Hola a todos los profesores y profesoras presentes también."
palabras=frase.split()
empty_dict={}
for palabra in palabras:
    if palabra in empty_dict:
        empty_dict[palabra]+=1
    else:
        empty_dict[palabra]=1
print(empty_dict)


# -----------------------------------
# Ejercicio 10
# Crea un pequeño sistema de inventario.
# El usuario puede ingresar productos y cantidades.
# Cuando escriba "done", el programa termina
# y muestra el inventario completo.
# -----------------------------------

print("Ejercicio 10:")
inventory={}

while True:
    product = input("Introduce el producto: ").capitalize()
    if product == "Done":
        break
    elif product in inventory:
        cantidad = int(input("Introduce la cantidad de productos: "))
        inventory[product]+=cantidad
    else:
        cantidad = int(input("Introduce la cantidad de productos: "))
        inventory[product]=cantidad
print(inventory)
