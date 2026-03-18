import random as r
import ecologia as eco
import operaciones as op


def main():
        lista = []
        for i in range(1,5):
            numeros = r.randint(1,10)
            lista.append(numeros)
        print(lista)

        suma=op.sumar(lista[0],lista[1])
        print(f"La suma de los dos primeros digitos es: {suma}")

        lista_animales = ["serpiente","gato", "perro", "iguana"]
        print(eco.contar_especies(lista_animales))
if __name__ == "__main__":
    main()