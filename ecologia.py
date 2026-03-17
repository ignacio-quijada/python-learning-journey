def contar_especies(lista):
    diccionario = {}
    for especie in lista:
        if especie not in diccionario:
            diccionario[especie]=+1
        else:
            diccionario[especie]+=1
    return diccionario