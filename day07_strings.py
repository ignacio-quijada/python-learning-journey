"""
Día 7 - Strings y Manipulación de Texto
Autor: Ignacio Quijada
Fecha: 2026-03-09
Descripción:
Ejercicios de Python enfocados en el trabajo con texto (strings).
Se practican métodos comunes como lower, upper, strip, replace, split y join.
"""

# -----------------------------------
# Ejercicio 1
# Pide al usuario su nombre y luego
# imprime el nombre en mayúsculas.
# -----------------------------------

print("Ejercicio 1:")

name=(input("Ingrese su nombre:")).upper()
print(name)

# -----------------------------------
# Ejercicio 2
# Pide una frase al usuario e imprime
# la misma frase en minúsculas.
# -----------------------------------

print("Ejercicio 2:")

text=input("Ingrese una frase:").lower()
print(text)

# -----------------------------------
# Ejercicio 3
# Pide una palabra al usuario e imprime
# cuántos caracteres tiene.
# -----------------------------------

print("Ejercicio 3:")

word=input("Ingrese una palabra:")
print(len(word))

# -----------------------------------
# Ejercicio 4
# Pide una frase al usuario y reemplaza
# todos los espacios por guiones "-".
# -----------------------------------

print("Ejercicio 4:")
text=input("Ingrese una frase:")
newtext=text.replace(" ","-")
print(newtext)

# -----------------------------------
# Ejercicio 5
# Pide una frase al usuario y muestra
# la primera y la última letra.
# -----------------------------------

print("Ejercicio 5:")

texto=input("Ingrese una frase:")
texto_separado=list(texto)
print(texto_separado[0], texto_separado[-1])


# -----------------------------------
# Ejercicio 6
# Pide una frase y cuenta cuántas veces
# aparece la letra "a".
# -----------------------------------

print("Ejercicio 6:")

texto=input("Ingrese una frase:")
conteo=texto.lower().count("a")
print(conteo)

# -----------------------------------
# Ejercicio 7
# Pide una frase y conviértela en una
# lista de palabras usando split().
# Luego imprime la lista.
# -----------------------------------

print("Ejercicio 7:")

texto=input("Ingrese una frase:")
lista=texto.split()
print(lista)

# -----------------------------------
# Ejercicio 8
# Dada una lista de palabras,
# únelas en una sola frase usando join().
# -----------------------------------

print("Ejercicio 8:")
lista=["Hola", "gente", "del", "mundo", "gaviota"]
union=" ".join(lista)
print(union)

# -----------------------------------
# Ejercicio 9
# Pide una frase y muestra cada palabra
# en una línea diferente usando un bucle.
# -----------------------------------

print("Ejercicio 9:")

texto=input("Ingrese una frase:")
lista=texto.split()
for i in lista:
    print(i)

# -----------------------------------
# Ejercicio 10
# Pide una frase al usuario y determina:
# - cuántas palabras tiene
# - cuál es la palabra más larga
# -----------------------------------

print("Ejercicio 10:")
texto=input("Ingrese una frase:")
lista=texto.split()
print(f"El texto tiene {len(lista)} palabras")
count=0
mas_larga=""
for i in lista:
    if len(i)>count:
        count=len(i)
        mas_larga=i
print(f"La palabra mas larga del texto es: {mas_larga}")