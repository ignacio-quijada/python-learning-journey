import math

import os

"""
El módulo os en Python sirve 
para interactuar con el sistema operativo, permitiendo gestionar archivos, 
directorios, rutas y variables de entorno de forma portátil entre Windows, Linux y macOS.
"""

def mostrar_bienvenida():

    print("===========================================")
    print("ECOLOGICAL BIODIVERSITY ANALYSIS")
    print("Author: Ignacio Quijada G.")
    print("===========================================\n")

def leer_observaciones():
    """
    Esta función lee el archivo de observaciones .txt
    elimina espacios y saltos de línea, y retorna la info
    en lista_de_observaciones
    """

    ruta = os.path.join(os.path.dirname(__file__), "observations.txt")

    """os.path.dirname(__file__) obtiene la carpeta donde se encuentra este script.
    os.path.join() construye la ruta al archivo de forma segura y compatible
    con cualquier sistema operativo, uniendo la carpeta del script con el nombre 
    del archivo "observations.txt"."""

    with open(ruta, "r", encoding="utf-8") as file:
        lista_observaciones = [line.strip() for line in file if line.strip()]

    return lista_observaciones

def contar_especies(lista_observaciones):

    """
    Recibe la lista de especies limpia y cuenta la
    riqueza de especies, agregando estas a un diccionario
    con su nombre científico y riqueza, depende totalmente
    del txt. Retorna rich_count, diccionario antes mencionado
    """

    rich_count = {}
    for species in lista_observaciones:
        if species in rich_count:
            rich_count[species] += 1
        else:
            rich_count[species] = 1
    return rich_count

def calcular_abundancia_relativa(lista_observaciones, rich_count):

    """
    Calcula la abundancia relativa, utilizando la cantidad de especies
    en lista_observaciones. La abundancia relativa se calcula dividiendo
    la cantidad de individuos de una especie entre la cantidad total de individuos
    observados. La función devuelve la abundancia relativa.
    Almacena este dato en un diccionario para cada especie.
    """

    relative_abundance = {}
    Σn_i = len(lista_observaciones)
    for clave, valor in rich_count.items():
        relative_abundance[clave] = valor / Σn_i
    return relative_abundance

def mostrar_indices():

    print("\nBiodiversity indices")
    print("-------------------------------")

def calcular_shannon(relative_abundance):

    """
    El índice de shannon utiliza la abundancia relativa, multiplicando
    esta por el logaritmo natural de este mismo. Estos valores se calculan
    para cada especie, siendo sumadas al final, y cambiando el signo de esta
    sumatoria. Se retorna el índice de shannon multiplicado por menos 1.

    """
    re_abXlog = {}
    for clave, valor in relative_abundance.items():
        re_abXlog[clave] = valor * math.log(valor)
    Σp_i = sum(re_abXlog.values())
    shannon_index = -Σp_i
    return shannon_index

def calcular_simpson(relative_abundance):

    """
    El índice de simpson también utiliza la abundancia relativa, elevando
    esta al cuadrado y restando 1. La dominancia es el valor elevado al
    cuadrado, sin restar 1. Esta función alacena ambos índices.
    """

    simpson_dict = {}
    for clave, valor in relative_abundance.items():
        simpson_dict[clave] = valor ** 2
    simpson_sum = (sum(simpson_dict.values()))
    simpson_index = 1 - simpson_sum

    return simpson_sum, simpson_index

def calcular_pielou(shannon_index, rich_count):
    """
    Esta funcion calcula el índice de Pielou, dividiendo el índice de
    shannon entre el logaritmo de la totalidad de observaciones. Devuelve
    el valor de J, para este índice.
    """
    j_index = (shannon_index / math.log(len(rich_count)))
    return j_index

def imprimir_resumen(lista_observaciones, rich_count):

    """
    Función que imprime el resumen de los datos obtenidos.
    """

    print("Dataset summary:")
    print("-------------------------------")
    print(f"Total observations: {len(lista_observaciones)}")
    richness = len(rich_count)
    print(f"Species richness: {richness}\n")
    print("Relative abundance per species:")
    print("-------------------------------")
    for clave, valor in rich_count.items():
        print(f"{clave}: {valor}\n")

def imprimir_indices(shannon_index, simpson_sum, simpson_index, j_index):

    print(f"Shannon index (H'): {shannon_index:.3f}")
    print(f"\nDominance (D): {simpson_sum:.3f}")
    print(f"\nSimpson index (1-D): {simpson_index:.3f}")
    print(f"\nPielou Evenness index (J'):{j_index:.2f}")

def interpretaciones(shannon_index, simpson_index, simpson_sum, j_index):
    print("\nEcological interpretation:")
    print("---------------------------")

    print("For Shannon diversity index (H'):")
    if shannon_index<1:
        print("Interpretation: Very low diversity")
    elif shannon_index<2:
        print("Interpretation: Low diversity")
    elif shannon_index<3:
        print("Interpretation: Moderate diversity")
    elif shannon_index<4:
        print("Interpretation: High diversity")
    else:
        print("Interpretation: Very high diversity")

    print("\nFor Simpson diversity index (1-D):")
    if simpson_index<0.5:
        print("Interpretation: The community has low diversity and is dominated by a few species.")
    elif simpson_index<0.75:
        print("Interpretation: “The community exhibits moderate diversity with a certain dominance of some species.”.")
    elif simpson_index<1:
        print("Interpretation: The community is highly diverse and species show relatively balanced abundances.")

    print("\nFor Pielou evenness index (J'):")
    if j_index<0.4:
        print("Interpretation: Low evenness. Abundances are strongly dominated by one or a few species.")
    elif j_index<0.6:
        print("Interpretation: Moderate equity. There is a moderately balanced distribution among species.")
    elif j_index<0.8:
        print("Interpretation: High equity. Species abundances are relatively balanced.")
    elif j_index<1:
        print("Interpretation: Very high equity. The abundances of the species are very similar to each other, indicating a highly balanced community.")

def main():
    mostrar_bienvenida()

    lista_observaciones = leer_observaciones()
    rich_count=contar_especies(lista_observaciones)
    relative_abundance=calcular_abundancia_relativa(lista_observaciones, rich_count)

    shannon_index=calcular_shannon(relative_abundance)
    simpson_sum,simpson_index=calcular_simpson(relative_abundance)
    j_index=calcular_pielou(shannon_index, rich_count)

    imprimir_resumen(lista_observaciones, rich_count)
    mostrar_indices()
    imprimir_indices(shannon_index, simpson_sum, simpson_index, j_index)
    interpretaciones(shannon_index, simpson_index, simpson_sum, j_index)

if __name__ == "__main__":
    main()