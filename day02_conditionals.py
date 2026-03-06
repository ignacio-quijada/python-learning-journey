"""
Día 2 - Condicionales (if, elif, else)
Autor: Ignacio Quijada
Fecha: 2026-03-06
Descripción:
Ejercicios de Python enfocados en estructuras condicionales.
Dificultad progresiva para practicar toma de decisiones en el código.
"""

# -----------------------------------
# Ejercicio 1 - Pide un número al usuario e indica si es positivo, negativo o cero.
# -----------------------------------

print("ejercicio 1:")
number=int(input("Ingrese un número: "))
if number  == 0:
    print("El número ingresado es cero")
elif number < 0:
    print(f"El número {number} es negativo!")
else:
    print(f"El número {number} es positivo!")


# -----------------------------------
# Ejercicio 2 - Pide un número e indica si es par o impar.
# -----------------------------------

print("ejercicio 2:")

number_a=int(input("Ingrese un número: "))
if number_a%2==0:
    print(f"El número {number_a} es par")
else:
    print(f"El número {number_a} es impar")


# -----------------------------------
# Ejercicio 3 - Pide dos números y muestra cuál es mayor.
# Si son iguales, indícalo.
# -----------------------------------

print("ejercicio 3:")
firstnumber=int(input("Ingrese un número: "))
secondnumber=int(input("Ingrese otro número: "))
if firstnumber > secondnumber:
    print(f"El número {firstnumber} es el mayor de los dos!")
elif firstnumber < secondnumber:
    print(f"El número {secondnumber} es el mayor de los dos!")
else:
    print("Los números son iguales!")


# -----------------------------------
# Ejercicio 4 - Pide la edad de una persona e indica si puede votar.
# En Chile se puede votar desde los 18 años.
# -----------------------------------

print("ejercicio 4:")
age=int(input("Ingrese su edad: "))
if age>=18:
    print(f"Su edad es {age}, puede votar segun la legislación chilena!")
elif age>0 and age<18:
    print(f"Según la legislación chilena, usted no cumple con la edad mínima para votar!")
else:
    print("No se ha ingresado una edad válida!")


# -----------------------------------
# Ejercicio 5 - Pide una nota de 1 a 7 e indica si el estudiante aprobó o reprobó.
# En Chile se aprueba con nota 4.0 o superior.
# -----------------------------------

print("ejercicio 5:")

grade=float(input("Ingrese su nota: "))

if grade>=4 and grade<=7:
    print("Usted ha aprobado, felicitaciones!")
elif grade>=1 and grade<4:
    print("Lo sentimos, usted ha reprobado!")
else:
    print("Usted no ha ingresado una nota válida!")


# -----------------------------------
# Ejercicio 6 - Pide tres números e indica cuál es el mayor.
# -----------------------------------

print("ejercicio 6:")

number_a=int(input("Ingrese su primer número: "))
number_b=int(input("Ingrese su segundo número: "))
number_c=int(input("Ingrese su tercer y último número: "))

if number_a>number_b and number_a>number_c:
    print(f"El primer número, '{number_a}', es el mayor de los tres!")
elif number_b>number_a and number_b>number_c:
    print(f"El segundo número, '{number_b}', es el mayor de los tres!")
elif number_a == number_b and number_a == number_c:
    print("Los tres números son iguales!")
else:
    print(f"El tercer número, '{number_c}', es el mayor de los tres!")


# -----------------------------------
# Ejercicio 7 - Pide una temperatura en grados Celsius.
# Clasifícala como:
# Frío (<10)
# Templado (10–25)
# Calor (>25)
# -----------------------------------

print("ejercicio 7:")
temperature=float(input("Ingrese la temperatura (C°): "))
if temperature<10:
    print(f"{temperature} grados Celsius se clasifica como temperatura fría!")
elif temperature>=10 and temperature<25:
    print(f"{temperature} grados Celsius se clasifica como temperatura templada!")
elif temperature>=25:
    print(f"{temperature} grados Celsius se clasifica como temperatura calurosa!")


# -----------------------------------
# Ejercicio 8 - Pide un número e indica:
# - "Divisible por 3"
# - "Divisible por 5"
# - "Divisible por ambos"
# - "No divisible por ninguno"
# -----------------------------------

print("ejercicio 8:")

numb=int(input("Ingrese el número: "))
if numb % 3 == 0 and numb % 5 == 0:
    print(f"El número {numb} es divisible por 3 y 5!")
elif numb % 3==0 and numb%5!=0:
    print(f"El número {numb} es divisible por 3!")
elif numb % 3!=0 and numb%5==0:
    print(f"El número {numb} es divisible por 5!")
else:
    print(f"El número {numb} no es divisible ni por 3 ni por 5!")


# -----------------------------------
# Ejercicio 9 - Crea un sistema simple de login.
# Usuario correcto: admin
# Contraseña correcta: 1234
# Indica si el acceso es permitido o denegado.
# -----------------------------------

print("ejercicio 9:")

usuario_correcto = "admin"
password_correcta = "1234"

user = input("Ingrese su usuario:")

if user == usuario_correcto:
    print("Usuario correcto.")

    passw = input("Ingrese su password:")

    if passw == password_correcta:
        print("Acceso concedido")
    else:
        print("Acceso denegado, contraseña incorrecta.")

else:
    print("Acceso denegado, usuario incorrecto.")



# -----------------------------------
# Ejercicio 10 - Pide la edad de una persona y clasifícala como:
# Niño (0–12)
# Adolescente (13–17)
# Adulto (18–59)
# Adulto mayor (60+)
# -----------------------------------

print("ejercicio 10:")

#7️⃣ Clasificación de edad

edad = int(input("Ingrese su edad para ser clasificado:"))

if edad < 0:
    print("Error, ingrese una edad correcta.")
elif edad >= 0 and edad <= 12:
    print("Usted es un niño")
elif edad >= 13 and edad <= 17:
    print("Usted es un adolescente")
elif edad >= 18 and edad < 59:
    print("Usted es un adulto")
elif edad >= 60:
    print("Usted es un adulto mayor")


