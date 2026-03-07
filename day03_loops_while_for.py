"""
Día 3 - Bucles (while y for)
Autor: Ignacio Quijada
Fecha: 2026-03-07
Descripción:
Ejercicios de Python enfocados en el uso de bucles while y for.
Se practican repeticiones, conteos y control de flujo.
"""

# -----------------------------------
# Ejercicio 1 - Imprime los números del 1 al 10 usando un bucle while.
# -----------------------------------

print("ejercicio 1:")
count=0
while count<10:
    count+=1
    print(count)


# -----------------------------------
# Ejercicio 2 - Imprime los números del 1 al 10 usando un bucle for.
# -----------------------------------

print("ejercicio 2:")

for numbers in range(1,11):
    print(numbers)


# -----------------------------------
# Ejercicio 3 - Pide un número al usuario e imprime la tabla de multiplicar de ese número del 1 al 10.
# -----------------------------------

print("ejercicio 3:")

number=int(input("Ingrese un numero para ver su tabla de multiplicar: "))
for i in range(1,11):
    print(f"{number} X {i} = {i*number}")


# -----------------------------------
# Ejercicio 4 - Pide un número e imprime todos los números pares desde 0 hasta ese número.
# -----------------------------------

print("ejercicio 4:")

par=int(input("Ingrese un número: "))
for i in range(0,(par+1)):
    if i % 2==0:
        print(i)

# -----------------------------------
# Ejercicio 5 - Pide números al usuario continuamente.
# El programa debe terminar cuando el usuario escriba "done".
# -----------------------------------

print("ejercicio 5:")

while True:
    num=input("Ingrese un número: ")
    if num=="done":
        break

# -----------------------------------
# Ejercicio 6 - Pide números al usuario hasta que escriba "done".
# Luego muestra la suma total de los números ingresados.
# -----------------------------------

print("ejercicio 6:")

count=0
while True:
    num=input("Ingrese un numero: ")
    if num=="done":
        break
    number=int(num)
    count=count+number
print(count)


# -----------------------------------
# Ejercicio 7 - Pide números al usuario hasta que escriba "done".
# Luego muestra el número mayor ingresado.
# -----------------------------------

print("ejercicio 7:")

count=0
while True:
    num=input("Ingrese un numero: ")
    if num=="done":
        break
    number=int(num)
    if number > count:
        count=number
print(f"El número mayor ingresado es: {count}")


# -----------------------------------
# Ejercicio 8 - Pide números al usuario hasta que escriba "done".
# Ignora entradas inválidas usando try/except.
# -----------------------------------

print("ejercicio 8:")

while True:

    num = input("Ingrese un numero: ")
    if num=="done":
        break
    try:
        number=float(num)
    except ValueError:
        print("Entrada no valida")
        continue


# -----------------------------------
# Ejercicio 9 - Imprime un triángulo de asteriscos como este:
#
# *
# **
# ***
# ****
# *****
#
# -----------------------------------

print("ejercicio 9:")

for i in range (1,6):
    print("*"*i)


# -----------------------------------
# Ejercicio 10 - Juego de adivinanza:
# El programa tiene un número secreto (por ejemplo 7).
# El usuario debe adivinarlo.
# El programa debe decir si el número es mayor o menor hasta que lo adivine.
# -----------------------------------

print("ejercicio 10:")


n_secreto=6

adivino=int(input("Adivina el número secreto:--->"))

while adivino != n_secreto:
    if adivino>n_secreto:
        print("el numero secreto es menor al que ingresaste")
    elif adivino<n_secreto:
        print("el numero secreto es mayor al que ingresaste")
        print("Vuelve a intentarlo!!")
    adivino = int(input("Adivina el número secreto:--->"))
print(f"Lo lograste! el numero era {n_secreto}")

