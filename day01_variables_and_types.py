"""
Día 1 - Variables y Tipos de Datos
Autor: Ignacio Quijada
Descripción:
Ejercicios básicos de Python sobre variables, tipos de datos y operaciones.
"""

# -----------------------------------
# Ejercicio 1- Crea tres variables: una de tipo str (nombre), una float (estatura) y una int (edad).
# -----------------------------------

print("ejercicio 1:")

nombre = "Ignacio"
edad = 28
altura = 1.60

print("Su nombre es:", nombre, "Su edad es:", edad, "y su altura es:", altura, "metros.\n")


# -----------------------------------
# Ejercicio 2-Crea dos variables enteras y guarda dos números.
# -----------------------------------

print("ejercicio 2")

numero1 = 25
numero2 = 2

print("la suma es:", numero1 + numero2)
print("la resta es:", numero1 - numero2)
print("la multiplicacion es:", numero1 * numero2)


# -----------------------------------
# Ejercicio 3
# -----------------------------------

print("ejercicio 3\n")

edad = input("Ingrese su edad:")
age = int(edad)

print("En 10 años tendrá:", age + 10, "años")


# -----------------------------------
# Ejercicio 4- imprimir tipos
# -----------------------------------

print("ejercicio 4")

a = 10
b = 3.14
c = "Hola"
d = True

print(type(a))
print(type(b))
print(type(c))
print(type(d))


# -----------------------------------
# Ejercicio 5 - Operacion entre 2 valores float, imprimir el valor redondeado con 2 decimales.
# -----------------------------------

print("ejercicio 5")

estatura1 = 1.76
estatura2 = 2.67

total = estatura1 / estatura2

print(round(total,2))


# -----------------------------------
# Ejercicio 6 - Concatenación de texto
# -----------------------------------

print("ejercicio 6")

nombre = "Juan"
apellido = "Ayala"

fullname = nombre + " " + apellido

print(fullname)


# -----------------------------------
# Ejercicio 7 - Booleanos
# -----------------------------------

print("ejercicio 7")

edad = 18

print(edad >= 18)


# -----------------------------------
# Ejercicio 8 -  Cambio de tipo de dato, pasar de str a int.
# -----------------------------------

print("ejercicio 8")

numero = "100"
nuevonumero = int(numero)

total = nuevonumero * 2

print(total)


# -----------------------------------
# Ejercicio 9- Intercambia sus valores sin escribir directamente los números nuevamente.
# Imprime el resultado final.
#Uso de Parallel Assignment
# -----------------------------------

print("ejercicio 9")

a = 5
b = 10

a,b = b,a

print(a)
print(b)


# -----------------------------------
# Ejercicio 10🔟 Cálculo simple
#
# Crea variables para:
#
# precio de un producto
#
# cantidad comprada
#
# Calcula el total a pagar y muéstralo en un mensaje como: El total a pagar es: $____
# -----------------------------------

print("ejercicio 10")

cantidad = int(input("Ingrese la cantidad comprada:"))
valor = 1999

print("El total a pagar es: $", cantidad * valor)