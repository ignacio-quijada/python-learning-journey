"""
Día 4 - Listas (Lists)
Autor: Ignacio Quijada
Fecha: 2026-03-07
Descripción:
Ejercicios de Python enfocados en el uso de listas.
Se practican creación, acceso, iteración y operaciones básicas.
"""

# -----------------------------------
# Ejercicio 1 - Crea una lista con 5 números e imprímela completa.
# -----------------------------------

print("ejercicio 1:")

name_list=[1,20,300,40,5]
print(name_list)



# -----------------------------------
# Ejercicio 2 - Crea una lista con 5 nombres e imprime solo el primer y el último elemento.
# -----------------------------------

print("ejercicio 2:")

name_list=["Jhon","Peter","Maria","Joseph","Ignacio"]
print(name_list[0],name_list[-1])
#Usé el [-1] que hace referencia siempre al último elemento de la lista, pero podría haber usado el índice [4].


# -----------------------------------
# Ejercicio 3 - Crea una lista de números e imprime cada número usando un bucle for.
# -----------------------------------

print("ejercicio 3:")
name_list=[1,10,15,20,25,30]
for number in name_list:
    print(number)


# -----------------------------------
# Ejercicio 4 - Pide 5 números al usuario y guárdalos en una lista.
# Luego imprime la lista completa.
# -----------------------------------

print("ejercicio 4:")

name_list=[]
for i in range(1,6):
    user_numbers=int(input("Ingrese un numero: "))
    name_list.append(user_numbers)

print(name_list)

# -----------------------------------
# Ejercicio 5 - Dada una lista de números, calcula la suma total usando un bucle.
# -----------------------------------

print("ejercicio 5:")

name_list=[240,22,55,40,100]
count=0
for number in name_list:
    count+=number
print(f"Total={count}")

# -----------------------------------
# Ejercicio 6 - Dada una lista de números, encuentra el número mayor.
# -----------------------------------

print("ejercicio 6:")

name_list=[24,22,25,20,27]
longest=name_list[0]
for number in name_list:
    if number>longest:
        longest=number
print(f"El número mayor es: {longest}")

# -----------------------------------
# Ejercicio 7 - Dada una lista de números, cuenta cuántos números pares hay.
# -----------------------------------

print("ejercicio 7:")
name_list=[24,22,25,20,27]
count=0
for number in name_list:
    if number%2==0:
        count+=1
print(f"Hay un total de {count} números pares")

# -----------------------------------
# Ejercicio 8 - Crea una lista de nombres.
# Si el nombre "Ignacio" está en la lista, imprime "Nombre encontrado".
# Si no está, imprime "Nombre no encontrado".
# -----------------------------------

print("ejercicio 8:")

name_list=["Juan","Pedro","Mark","Humberto"]
if "Ignacio" in name_list:
    print("Nombre encontrado")
else:
    print("Nombre no encontrado")

# -----------------------------------
# Ejercicio 9 - Crea una lista de números y genera una nueva lista
# que contenga solo los números mayores que 10.
# -----------------------------------

print("ejercicio 9:")
name_list=[1,22,3,5,1,2,3,1,2,23,3,2,3,1,23,1,23,1,2,3,3,3,8,4,5,4235,34,5,80,213,42,9,1,123]
new_list=[]
for number in name_list:
    if number>10:
        new_list.append(number)
print(f"Nueva lista con valores mayores a 10: {new_list}")


# -----------------------------------
# Ejercicio 10 - Pide números al usuario hasta que escriba "done".
# Guarda los números en una lista y luego imprime:
# - la cantidad de números
# - el número mayor
# - el número menor
# -----------------------------------

print("ejercicio 10:")

name_list=[]
while True:
    entr_nmbrs=input("Ingrese valores: ")
    if entr_nmbrs.lower()=="done":
        break
    try:
        number=int(entr_nmbrs)
        name_list.append(number)
    except ValueError:
        print("Valor invalido")
longest=None
lowest=None
for numbers in name_list:
    if longest is None or numbers>longest:
        longest=numbers
    if lowest is None or numbers<lowest:
        lowest=numbers
print(f"Cantidad total de números: {len(name_list)}")
print(f"El número mayor es: {longest}")
print(f"El número menor es: {lowest}")

