def contar_especies(lista):
    diccionario = {}
    for especie in lista:
        if especie not in diccionario:
            diccionario[especie]=1
        else:
            diccionario[especie]+=1
    return diccionario

if __name__ == "__main__":
#prueba de contar_especies
    lista = ["gato","gato","perro"]
    print(contar_especies(lista))