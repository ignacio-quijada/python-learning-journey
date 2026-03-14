

"""
Día 9 - Manejo de errores (try / except)
Autor: Ignacio Quijada
Fecha: 2026-03-15

Descripción:
Ejercicios enfocados en el manejo de errores en Python utilizando
try / except para evitar que los programas se detengan cuando
ocurren errores durante la ejecución.

Se induce al error para identificar este antes de escribir el except.
"""

# -----------------------------------
# Ejercicio 1
# Pide al usuario que ingrese un número entero.
# Si el usuario ingresa algo que no sea un número,
# muestra el mensaje:
# "Entrada inválida. Debes ingresar un número entero."
# -----------------------------------

print("Ejercicio 1:")

entrada=input("Introduce un numero: ")
try:
    numero = int(entrada)
    print(f"Numero válido: {numero}")
except ValueError:
    print("Entrada inválida. Debes ingresar un número entero.")

# -----------------------------------
# Ejercicio 2
# Pide al usuario dos números.
# Calcula la división entre ellos.
# Debes manejar:
# - error si el usuario escribe texto
# - error si intenta dividir por cero
# -----------------------------------

print("Ejercicio 2:")
entrada_a=input("Introduce un numero: ")
entrada_b=input("Introduce otro numero: ")
try:
    numero_a=int(entrada_a)
    numero_b=int(entrada_b)
    resultado=numero_a/numero_b
    print(f"Resultado es: {resultado}")
except ValueError:
    print("Entrada no válida, ingrese un numero entero.")
except ZeroDivisionError:
    print("No es posible dividir por 0")


# -----------------------------------
# Ejercicio 3
# Pide al usuario que ingrese 5 números.
# Si el usuario ingresa algo inválido,
# muestra "Entrada inválida" y vuelve a pedir el número.
# Al final muestra la suma total.
# -----------------------------------

print("Ejercicio 3:")

lista=[]
count=1
while count<6:
    entrada=input("Introduce un numero: ")
    try:
        numero=int(entrada)
        lista.append(numero)
        count += 1
    except ValueError:
        print("Entrada inválida")


print(f"La suma es: {sum(lista)}")


# -----------------------------------
# Ejercicio 4
# Crea una lista con los siguientes elementos:
# ["perro", "gato", "conejo", "hamster"]
#
# Pide al usuario un índice.
# Si el índice no existe, muestra:
# "Índice fuera de rango."
# -----------------------------------

print("Ejercicio 4:")

lista=["perro", "gato", "conejo", "hamster"]

entrada=input("Introduce un numero: ")

try:
    numero = int(entrada)
    print(f"El índice {numero} es: {lista[numero]}")

except IndexError:
        print("Índice fuera de rango.")
        
except ValueError:
    print("Ingrese un numero entero (índice).")


# -----------------------------------
# Ejercicio 5
# Tienes la siguiente lista:
# ["10", "25", "hola", "8", "42", "error"]
#
# Intenta convertir cada elemento a entero.
# Si no se puede convertir, muestra:
# "No se pudo convertir: X"
#
# Al final crea una nueva lista solo con los
# números válidos.
# -----------------------------------

print("Ejercicio 5:")

lista= ["10", "25", "hola", "8", "42", "error"]
nueva_lista=[]
for numero in lista:

    try:
        nuevo_numero=int(numero)
        nueva_lista.append(nuevo_numero)
    except ValueError:
        print(f"No se pudo convertir: {numero}")
print(nueva_lista)

# -----------------------------------
# Ejercicio 6
# Intenta abrir el archivo "datos.txt".
# Si el archivo no existe, muestra:
# "El archivo no fue encontrado."
# -----------------------------------

print("Ejercicio 6:")

try:
    with open("datos.txt","r",encoding="utf-8") as archivo:
        print(archivo.read())
        
except FileNotFoundError:
    print("el archivo no fue encontrado")

# -----------------------------------
# Ejercicio 7
# Crea una calculadora simple.
#
# El programa debe pedir:
# - número 1
# - número 2
# - operación (+, -, *, /)
#
# Maneja errores de:
# - entrada inválida
# - división por cero
# -----------------------------------

print("Ejercicio 7:")

entrada_a=input("Introduce un numero: ")
entrada_b=input("Introduce otro numero: ")
print('Operaciones disponibles:"+" "-" "*" "/"')

operacion=input("Introduce operacion: ")

try:
    numero_a=int(entrada_a)
    numero_b=int(entrada_b)

    if operacion=="+":
            print(numero_a+numero_b)
    elif operacion=="-":
            print(numero_a-numero_b)
    elif operacion=="*":
            print(numero_a*numero_b)
    elif operacion=="/":
            print(numero_a/numero_b)
    else:
            print("Operacion invalida")
except ZeroDivisionError:
    print("No se puede dividir por cero")
except ValueError:
    print("entrada inválida")


# -----------------------------------
# Ejercicio 8
# Pide números al usuario hasta que escriba "done".
# Calcula el promedio de los números ingresados.
#
# Si el usuario escribe algo inválido,
# muestra "Entrada inválida".
# -----------------------------------

print("Ejercicio 8:")

lista=[]

while True:
    entrada=input("Introduce un numero: ")
    if entrada == "done":
        break
    try:
        numero=int(entrada)
        lista.append(numero)
    except ValueError:
        print("Entrada invalida")
        
if len(lista)>0:
    suma = sum(lista)
    total = suma / len(lista)
    print(f"Promedio: {total}")
else:
    print("No se ingresaron numeros")

# -----------------------------------
# Ejercicio 9
# Crea el siguiente diccionario:
#
# {
# "perro": "dog",
# "gato": "cat",
# "caballo": "horse"
# }
#
# Pide al usuario una palabra en español
# y muestra su traducción al inglés.
#
# Si la palabra no está en el diccionario,
# muestra:
# "Palabra no encontrada."
# -----------------------------------

print("Ejercicio 9:")

diccionario={
    "perro": "dog",
    "gato": "cat",
    "caballo": "horse"
}
entrada=input("Introduce un nombre: ").lower()
try:
    print(diccionario[entrada])
except KeyError:
    print("Palabra no encontrada")


# -----------------------------------
# Ejercicio 10
# Pide al usuario una lista de números separados
# por coma, por ejemplo:
#
# 10,20,30,40
# Convierte los valores a números y calcula
# el promedio.
# Si algún valor no es válido, muestra:
# "Valor inválido detectado."
# -----------------------------------
lista_1 = []
csv = input("Introduce la lista: ")
entrada = csv.split(",")

for caracteres in entrada:
    try:
        convertir=int(caracteres)
        lista_1.append(convertir)
        print(f"...Agregado: {convertir} OK")
    except ValueError:
        print(f"Valor invalido detectado: {caracteres}")

if len(lista_1)>0:
    suma=sum(lista_1)
    total=suma/len(lista_1)
    print(f"el promedio es: {total}")
else:
    print("No se pudieron procesar números válidos")