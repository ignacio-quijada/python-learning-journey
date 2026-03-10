"""
Día 8 - Manejo de Archivos (File Handling)
Autor: Ignacio Quijada
Fecha: 2026-03-10
Descripción:
Ejercicios de Python enfocados en leer y escribir archivos.
Se practican open(), read(), write() y manejo básico de texto desde archivos.
"""

# -----------------------------------
# Ejercicio 1
# Crea un archivo llamado "mensaje.txt"
# y escribe dentro el texto:
# "Hola, este es mi primer archivo creado con Python".
# -----------------------------------

print("Ejercicio 1:")
with open("mensaje.txt","w", encoding="utf-8") as fichero:
    fichero.write("Hola, este es mi primer archivo creado con Python")

# -----------------------------------
# Ejercicio 2
# Abre el archivo "mensaje.txt"
# y muestra su contenido en pantalla.
# -----------------------------------

print("Ejercicio 2:")

with open("mensaje.txt","r", encoding="utf-8") as fichero:
    print(fichero.read())


# -----------------------------------
# Ejercicio 3
# Pide al usuario una frase
# y guárdala en un archivo llamado
# "frases.txt".
# -----------------------------------

print("Ejercicio 3:")

frase=input("Ingrese una frase:").capitalize()
with open("frases.txt","w", encoding="utf-8") as fichero:
    fichero.write(frase+"\n")

# -----------------------------------
# Ejercicio 4
# Pide al usuario varias frases.
# El programa termina cuando escriba "done".
# Guarda todas las frases en "frases.txt".
# -----------------------------------

print("Ejercicio 4:")
lista_frases=[]
while True:
    frase=input("Ingrese una frase:>>>")
    if frase == "done":
        break
    lista_frases.append(frase)
with open("frases.txt","a", encoding="utf-8") as fichero:
    for frases in lista_frases:
        fichero.write(frases+"\n")

# -----------------------------------
# Ejercicio 5
# Abre el archivo "frases.txt"
# y muestra cada línea por separado.
# -----------------------------------

print("Ejercicio 5:")

with open("frases.txt","r", encoding="utf-8")as fichero:
    print(fichero.read())

# -----------------------------------
# Ejercicio 6
# Cuenta cuántas líneas tiene
# el archivo "frases.txt".
# -----------------------------------

print("Ejercicio 6:")
lista=[]
with open("frases.txt","r", encoding="utf-8")as fichero:
   for frase in fichero:
       lista.append(frase)
print(len(lista))

# -----------------------------------
# Ejercicio 7
# Cuenta cuántas palabras hay
# en todo el archivo "frases.txt".
# -----------------------------------

print("Ejercicio 7:")

with open("frases.txt","r", encoding="utf-8")as fichero:
    texto=fichero.read()
    palabras=texto.split()
print(len(palabras))