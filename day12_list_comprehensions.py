"""
DÍA 12 - LIST COMPREHENSIONS

Instrucciones:
Completa cada ejercicio usando list comprehensions cuando sea posible.
Evita usar loops tradicionales (for) a menos que sea necesario.
"""

# =========================
# EJERCICIO 1
# =========================
# Crea una lista con los números del 1 al 20
# Luego crea otra lista con solo los números pares
print("Ejercicio 1:")

numeros = list(range(1, 21))
pares = [i for i in numeros if i%2==0]
print(f"1) Pares: {pares}")


# =========================
# EJERCICIO 2
# =========================
# Dada esta lista, crea una nueva con los números elevados al cuadrado
print("Ejercicio 2:")

nums = [1, 2, 3, 4, 5]

cuadrados = [x**2 for x in nums]

print(f"2) Cuadrados:{cuadrados}")


# =========================
# EJERCICIO 3
# =========================
# Filtra solo los números mayores a 10
print("Ejercicio 3:")

lista = [5, 12, 7, 18, 3, 20]

mayores = [x for x in lista if x >10]

print(f"3) Mayores a 10:{mayores}")


# =========================
# EJERCICIO 4
# =========================
# Convierte esta lista de strings a mayúsculas

palabras = ["python", "java", "c", "javascript"]

mayus = [palabra.upper() for palabra in palabras]

print(f"4) Mayúsculas: {mayus}")


# =========================
# EJERCICIO 5
# =========================
# De esta lista, deja solo las palabras que tengan más de 4 letras

words = ["sol", "computadora", "mesa", "teclado", "luz"]

largas = [x for x in words if len(x) > 4]

print(f"5) Palabras largas:{largas}")


# =========================
# EJERCICIO 6
# =========================
# Crea una lista de tuplas (número, "par"/"impar")

nums2 = [1, 2, 3, 4, 5]

paridad = [(x,"par") if x%2==0 else (x,"impar") for x in nums2]

print(f"6) Paridad:{paridad}")


# =========================
# EJERCICIO 7
# =========================
# Aplana esta lista de listas en una sola lista

lista_de_listas = [[1, 2], [3, 4], [5, 6]]

plana = [x for sublist in lista_de_listas for x in sublist]  # COMPLETAR

print(f"7) Lista plana:{plana}")


# =========================
# EJERCICIO 8
# =========================
# Genera una lista con los números del 1 al 30 que sean múltiplos de 3

multiplos = [x for x in range (1,31) if x%3==0]  # COMPLETAR
print("8) Múltiplos de 3:", multiplos)


# =========================
# EJERCICIO 9
# =========================
# Reemplaza los números negativos por 0

nums3 = [5, -3, 8, -1, 0, -7]

sin_negativos = [0 if x<0 else x for x in nums3]  # COMPLETAR

print("9) Sin negativos:", sin_negativos)


# =========================
# EJERCICIO 10
# =========================
# Dada esta lista, crea un diccionario donde:
# clave = número
# valor = número al cuadrado

nums4 = [1, 2, 3, 4]

diccionario = {x:x**2 for x in nums4}  # COMPLETAR

print("10) Diccionario:", diccionario)