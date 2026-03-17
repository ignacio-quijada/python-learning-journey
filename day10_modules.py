"""
Día 10 - Módulos en Python
Autor: Ignacio Quijada
Fecha: 2026-03-16

Descripción:
Ejercicios enfocados en el uso de módulos en Python.
Se busca aprender a dividir el código en múltiples archivos
y reutilizar funciones mediante importaciones.
"""

# -----------------------------------
# Ejercicio 1
# Crea un archivo llamado "saludos.py"
# con una función:
#
# saludar(nombre)
#
# que imprima:
# "Hola, [nombre]!"
#
# Luego importa la función en este archivo
# y pruébala.
# -----------------------------------

print("Ejercicio 1:")
from saludos import saludar
saludar("Ignacio")

# -----------------------------------
# Ejercicio 2
# Crea un archivo "operaciones.py" con funciones:
#
# sumar(a, b)
# restar(a, b)
# multiplicar(a, b)
# dividir(a, b)
#
# Luego importa el módulo y prueba cada función.
# -----------------------------------

print("Ejercicio 2:")

import operaciones as op
print(op.sumar(1, 1))
print(op.restar(10, 5))
print(op.multiplicar(5, 2))
print(op.dividir(5, 5))

# -----------------------------------
# Ejercicio 3
# Desde el módulo "operaciones.py",
# importa solo la función "sumar"
# y utilízala.
# -----------------------------------

print("Ejercicio 3:")

from operaciones import sumar
print(sumar(150, 150))


# -----------------------------------
# Ejercicio 4
# Importa el módulo "operaciones.py"
# usando un alias (por ejemplo: op)
# y utiliza sus funciones.
# -----------------------------------

print("Ejercicio 4:")

import operaciones as op
print(op.sumar(150, 150))
print(op.restar(150, 50))
print(op.multiplicar(50, 50))
print(op.dividir(100, 50))


# -----------------------------------
# Ejercicio 5
# Crea un módulo llamado "conversiones.py"
# con funciones:
#
# celsius_a_fahrenheit(c)
# metros_a_kilometros(m)
#
# Luego impórtalo y prueba ambas funciones.
# -----------------------------------

print("Ejercicio 5:")
import conversiones as conv
print(conv.celsius_a_fahrenheit(30))
print(conv.metros_a_kilometros(1000))

# -----------------------------------
# Ejercicio 6
# Crea un módulo llamado "ecologia.py"
# con una función:
#
# contar_especies(lista)
#
# que reciba una lista de especies y devuelva
# un diccionario con el conteo de cada una.
#
# Luego importa y prueba la función.
# -----------------------------------

print("Ejercicio 6:")
import ecologia as eco
lista=["gato", "perro", "zancudo", "gato", "comadreja", "zorro", "perro", "comadreja"]

print(eco.contar_especies(lista))


# -----------------------------------
# Ejercicio 7
# Desde el módulo "ecologia.py",
# importa la función contar_especies
# y úsala con una lista de ejemplo.
# -----------------------------------

print("Ejercicio 7:")

import ecologia as eco
print(eco.contar_especies(lista))


# -----------------------------------
# Ejercicio 8
# Usa el módulo estándar "math"
# para:
#
# - calcular la raíz cuadrada
# - calcular logaritmos
#
# Imprime los resultados.
# -----------------------------------

print("Ejercicio 8:")

import math as m
print(m.sqrt(36))
print(m.log10(10))

# -----------------------------------
# Ejercicio 9
# Usa el módulo "random" para:
#
# - generar un número aleatorio entre 1 y 100
# - elegir un elemento aleatorio de una lista
#
# -----------------------------------

print("Ejercicio 9:")

lista = [1,5,6,78,2,3,75,67,5,3,4,12,324]

import random as r

print(r.randint(1, 100))
print(r.choice(lista))

#-----------------------------------
# Ejercicio 10
# (Mini proyecto simple con módulos)
#
# Usa los módulos que creaste anteriormente
# para construir un pequeño programa que:
#
# 1. Tenga una lista de números
# 2. Calcule:
#    - suma (usando operaciones.py)
#    - promedio (puedes calcularlo tú)
#
# 3. Muestre los resultados en pantalla
#
# Ejemplo de salida esperada:
#
# Lista: [10, 20, 30]
# Suma: 60
# Promedio: 20.0
#
# Objetivo:
# Practicar cómo reutilizar funciones desde módulos
# en un programa principal.
# -----------------------------------
print("Ejercicio 10:")

import operaciones as op
import random as r


lista_numeros = []

for i in range (3):
    numero_random = r.randint(1, 100)
    lista_numeros.append(numero_random)

print(f"Lista: {lista_numeros}")

resultado = op.sumar(lista_numeros[0], lista_numeros[1]) + lista_numeros[2]
print(f"Suma: {resultado}")

promedio = resultado / len(lista_numeros)
print(f"Promedio: {promedio}")