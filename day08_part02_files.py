# -----------------------------------
# Ejercicio 8
# Encuentra la palabra más larga
# dentro del archivo "frases.txt".
# -----------------------------------

print("Ejercicio 8:")

with open("frases.txt",encoding="utf-8") as file:
    texto=file.read()
    splitted_texto=texto.split()

    count = 0
    palabra_larga=[]
    for palabra in splitted_texto:
        if len(palabra)>count:
            count=len(palabra)
            palabra_larga=palabra

print(f"La palabra mas larga del texto es: {palabra_larga}")

# -----------------------------------
# Ejercicio 9
# Crea un archivo "numeros.txt"
# y guarda los números del 1 al 20
# cada uno en una línea diferente.
# -----------------------------------

print("Ejercicio 9:")

with open("numeros.txt","w",encoding="utf-8") as file:
        for numero in range(1,21):
            linea=str(numero)+"\n"
            file.write(linea)


# -----------------------------------
# Ejercicio 10
# Lee el archivo "numeros.txt"
# y calcula la suma de todos los números.
# -----------------------------------

print("Ejercicio 10:")
with open("numeros.txt","r",encoding="utf-8") as file:

    nuevo_numero=map(int,file)
    total=0
    for numero in nuevo_numero:
        total= total+numero
print(total)

