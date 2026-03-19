"""
Día 11 - __name__ == "__main__"
Autor: Ignacio Quijada
Fecha: 2026-03-18

Descripción:
Ejercicios enfocados en entender el comportamiento de ejecución
de archivos Python y el uso de:

if __name__ == "__main__":

para controlar qué código se ejecuta al correr un script
y qué código se ejecuta al importar módulos.
"""

# -----------------------------------
# Ejercicio 1
# Imprime el valor de __name__.
# Ejecuta este archivo directamente.
# -----------------------------------

print("Ejercicio 1:")

print(__name__)


# -----------------------------------
# Ejercicio 2
# Crea un archivo llamado "test_modulo.py"
# que imprima __name__.
#
# Luego:
# - ejecútalo directamente
# - impórtalo desde este archivo
#
# Observa la diferencia.
# -----------------------------------

print("Ejercicio 2:")

#import test_modulo


# -----------------------------------
# Ejercicio 3
# En "test_modulo.py", agrega:
#
# if __name__ == "__main__":
#     print("Ejecutado directamente")
#
# Luego:
# - ejecútalo
# - impórtalo
#
# Observa qué cambia.
# -----------------------------------

print("Ejercicio 3:")

import test_modulo

# -----------------------------------
# Ejercicio 4
# Crea una función en "test_modulo.py":
#
# def saludar():
#     print("Hola desde módulo")
#
# Llama la función solo dentro de:
#
# if __name__ == "__main__":
#
# Luego impórtala y ejecútala desde aquí.
# -----------------------------------

print("Ejercicio 4:")

from test_modulo import saludar
saludar()

# -----------------------------------
# Ejercicio 5
# Modifica tu archivo "operaciones.py"
# para que tenga un bloque:
#
# if __name__ == "__main__":
#     # pruebas de funciones
#
# Dentro prueba sumar, restar, etc.
# -----------------------------------

print("Ejercicio 5:")

import operaciones


# -----------------------------------
# Ejercicio 6
# Importa "operaciones.py" en este archivo
# y usa sus funciones.
#
# Verifica que el código dentro de
# if __name__ == "__main__"
# NO se ejecute.
# -----------------------------------

print("Ejercicio 6:")

import operaciones



# -----------------------------------
# Ejercicio 7
# Modifica "ecologia.py" agregando:
#
# if __name__ == "__main__":
#     # prueba de contar_especies
#
# Luego impórtalo y verifica comportamiento.
# -----------------------------------

print("Ejercicio 7:")

from ecologia import contar_especies
lista = ["gato","tortuga","perro"]

print(contar_especies(lista))


# -----------------------------------
# Ejercicio 8
# Crea un archivo "main.py"
#
# Este archivo debe:
# - importar tus módulos
# - ejecutar funciones principales
#
# Este será tu "programa principal".
# -----------------------------------

print("Ejercicio 8:")



# -----------------------------------
# Ejercicio 9
# En "main.py", usa:
#
# if __name__ == "__main__":
#     # ejecutar programa
#
# Asegúrate de que nada se ejecute
# automáticamente al importar.
# -----------------------------------

print("Ejercicio 9:")

import main as m

# -----------------------------------
# Ejercicio 10
# (Mini integración)
#
# Crea un flujo donde:
#
# - main.py controla la ejecución
# - usa funciones de:
#   - operaciones.py
#   - ecologia.py
#
# Ejemplo:
# - calcular suma
# - contar especies
#
# Todo debe ejecutarse SOLO si:
# main.py es el archivo principal
#
# Objetivo:
# Simular estructura real de proyecto.
# -----------------------------------

print("Ejercicio 10:")

m.main()
