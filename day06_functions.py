"""
Día 6 - Funciones (Functions)
Autor: Ignacio Quijada
Fecha: 2026-03-08
Descripción:
Ejercicios de Python enfocados en el uso de funciones.
Se practican definición de funciones, parámetros y retorno de valores.
"""

# -----------------------------------
# Ejercicio 1
# Crea una función llamada saludo()
# que imprima "Hola, bienvenido a Python".
# Luego llama la función.
# -----------------------------------

print("Ejercicio 1:")
def saludo():
    print("Hola, bienvenido a Python")
saludo()

# -----------------------------------
# Ejercicio 2
# Crea una función llamada saludar(nombre)
# que reciba un nombre y lo imprima así:
# "Hola, <nombre>"
# -----------------------------------

print("Ejercicio 2:")
def saludar(nombre):
    print(f"Hola, {nombre}")

saludar("Ignacio")

# -----------------------------------
# Ejercicio 3
# Crea una función suma(a, b)
# que reciba dos números y devuelva la suma.
# Luego imprime el resultado.
# -----------------------------------

print("Ejercicio 3:")

def suma(a,b):
    return a+b
print(suma(10,5))

# -----------------------------------
# Ejercicio 4
# Crea una función es_par(numero)
# que devuelva True si el número es par
# y False si es impar.
# -----------------------------------

print("Ejercicio 4:")

def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

print(es_par(22))

# -----------------------------------
# Ejercicio 5
# Crea una función mayor(a, b)
# que devuelva el número mayor.
# -----------------------------------

print("Ejercicio 5:")

def mayor(a,b):
    if a>b:
        print(f"{a} es mayor que {b}")
    elif a==b:
        print("Los números son iguales")
    else:
        print(f"{a} es menor que {b}")
mayor(21,23)
# -----------------------------------
# Ejercicio 6
# Crea una función contar_letras(palabra)
# que devuelva la cantidad de letras
# que tiene la palabra.
# -----------------------------------

print("Ejercicio 6:")

def contar_letras(palabra):
    print(f"La palabra {palabra} tiene {len(palabra)} letras")
    return len(palabra)
contar_letras("Ignacio")

# -----------------------------------
# Ejercicio 7
# Crea una función lista_pares(lista)
# que reciba una lista de números
# y devuelva una nueva lista con solo
# los números pares.
# -----------------------------------

print("Ejercicio 7:")

lista = [1,2,20,22,24,3,4,5,6,97]
def lista_pares(lista):
    lista_vacia = []
    for numeros in lista:
        if numeros % 2 == 0:
            lista_vacia.append(numeros)
    return lista_vacia
print(lista_pares(lista))

# -----------------------------------
# Ejercicio 8
# Crea una función promedio(lista)
# que reciba una lista de números
# y devuelva el promedio.
# -----------------------------------

print("Ejercicio 8:")
lista=[1,2,4,5,7,3,1,6,8,6,4]
def promedio(lista):
    count=0
    for numeros in lista:
        count+=numeros
    total=count/len(lista)
    return (f"El promedio es {total}")
print(promedio(lista))

# -----------------------------------
# Ejercicio 9
# Crea una función contar_palabras(texto)
# que reciba una frase y devuelva
# cuántas palabras tiene.
# -----------------------------------

print("Ejercicio 9:")
texto=("Ignacio está aprendiendo los principios de python.")
def contar_palabras(texto):
    div_texto=texto.replace(".",",").split()
    longitud_texto=len(div_texto)
    return (f"El texto tiene {longitud_texto} palabras")
print(contar_palabras(texto))

# -----------------------------------
# Ejercicio 10
# Crea una función calculadora(a, b, operacion)
# operaciones posibles:
# "suma"
# "resta"
# "multiplicacion"
# "division"
#
# La función debe devolver el resultado
# según la operación indicada.
# -----------------------------------

print("Ejercicio 10:")

#print("Calculadora, digite los números que desea operar:")
#a=int(input("Elija el primer número:>>>"))
#b=int(input("Elija el segundo número:>>>"))
#operacion=input("Escriba suma, resta, multiplicacion o division:").lower()

def calculadora(a, b, operacion):

    if operacion=="suma":
        return a+b
    elif operacion=="resta":
        return a-b
    elif operacion=="multiplicacion":
        return a*b
    elif operacion=="division":
        if b==0:
            return("No se puede dividir por 0")
        return a/b
    else:
        return ("Operacion no válida")

print(calculadora(2,3,"suma"))