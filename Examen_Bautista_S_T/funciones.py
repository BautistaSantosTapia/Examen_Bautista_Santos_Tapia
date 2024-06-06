import random
import os
import json

def menu()->str:
    """despliega el menu de opciones en formato amigable para el usuario

    Returns:
        str: un pedido de accion para el usuario
    """
    limpiar_pantalla()
    print(f"{'Menu de Opciones':^50s}")
    print("1- Cargar archivo .CSV")
    print("2- Imprimir lista")
    print("3- Asignar rating")
    print("4- Asignar género")
    print("5- Filtrar por género")
    print("6- Ordenar películas")
    print("7- Informar Mejor Rating")
    print("8- Guardar películas")
    print("9- Salir")
    return input("Ingrese opcion: ")

def pausar():
    """lo pausa
    """
    import os
    os.system("pause")

def limpiar_pantalla():
    """lo limpia para que no lo veas repetido
    """
    import os 
    os.system("cls")


#1) Cargar archivo .CSV: Se pedirá el nombre del archivo y se cargará en una lista de diccionarios los elementos del mismo.

def cargar_archivo_csv(nombre_archivo:str):
    """la funcion lee un archivo csv y lo pasa a una lista de diccionarios

    Args:
        nombre_archivo (str): el nombre del archivo

    Returns:
        _type_: retorna la lista con los diccionarios
    """
    directorio_actual = os.path.dirname(__file__)
    path = os.path.join(directorio_actual, nombre_archivo)

    with open(path, mode= "r", encoding= "utf-8") as archivo:
        lista_datos = []
        encabezado = archivo.readline().strip("\n").split(",")

        for linea in archivo.readlines(): 
            pelicula = {}
            linea = linea.strip("\n").split(",")

            id,titulo,genero,rating = linea
            pelicula["id"] = int(id)
            pelicula["titulo"] = titulo
            pelicula["genero"] = genero
            pelicula["rating"] = int(rating)
            lista_datos.append(pelicula)

    return lista_datos



# 2) Imprimir lista: Se imprimirá por pantalla la tabla con los datos de las películas.

def mostrar_item_pelicula(una_pelicula:dict):
    """muestra los values de un item de la lista

    Args:
        una_pelicula (dict): es una pelicula en particular 
    """
    print(f'{una_pelicula["id"]:>3} {una_pelicula["titulo"]:>30}   {una_pelicula["genero"]:>8}    {una_pelicula["rating"]:4.1f}')

def mostrar_lista(lista:list)->None:
    """te muestra toda la lista de una forma mas amigable

    Args:
        lista (list): es la lista que queres que muestre
    """
    print("***Listado peliculas***")
    print("  id                titulo            genero     rating")
    print("------------------------------")
    for i in range(len(lista)):
        mostrar_item_pelicula(lista[i])
    print()



    
#3) Asignar rating: Se deberá hacer uso de la función map. La cual recibirá la lista y una función que asignará a la película un valor de rating flotante entre 1 y 10 con 1 decimal calculado de manera aleatoria se mostrará por pantalla el mismo.

def asignar_rating(lista:list):
    """le genera un rating a cada pelicula

    Args:
        lista (list): es la lista a la que le queres pasar los ratings

    Returns:
        _type_: te retorna una lista con los ratings ya creados
    """
    lista_retorno = []
    for peli in lista:
        entero = random.randint(1,9)
        decimal = random.randint(0,9)
        peli["rating"] = float(f"{entero}.{decimal}")
        lista_retorno.append(peli)
    return lista_retorno




# 4) Asignar género: Se deberá hacer uso de la función map. La cual recibirá la lista y una
# función que asignará a la película un género de acuerdo a un número aleatorio entre 1 y 4.
# 1: drama
# 2: comedia
# 3: acción
# 4: terror
def asignar_genero(lista:list, g_list:list):
    """se le asigna un genero de entre una lista a cada elemento de la otra lista

    Args:
        lista (list): la lista a la que queres que le asignen los generos
        g_list (list): la lista con los generos
    """
    for peli in lista:
        num_random = random.randint(1,4)
        peli["genero"] = g_list[num_random - 1]


        

# 5) Filtrar por género: Se deberá pedir un género y escribir un archivo igual al original, pero donde solo aparezcan películas del género seleccionado. El nombre del archivo será p.e. comedias.csv
def pelicula_genero(lista:list,genero:str)->list:
    """hace una lista con un tipo de genero en especifico

    Args:
        lista (list): la lista que queres tarbajar
        genero (str): el genero en especifico que te interesa

    Returns:
        list: una lista con solo as peliculas que cumplan el genero especificado
    """
    lista_pelis = []
    for peli in lista:
        if genero == peli["genero"]:
            lista_pelis.append(peli)
    return lista_pelis


def archivo_genero(nombre_archivo:str, lista:list):
    """genera un archivo csv con la lista de generos de la funcion de arriba

    Args:
        nombre_archivo (str): el nombre que le quieras dar al archivo
        lista (list): la lista con los elementos que quieras guardar
    """
    directorio_actual = os.path.dirname(__file__)
    path = os.path.join(directorio_actual, nombre_archivo)

    with open(path, mode= "w", encoding="utf-8") as archivo:

        keys = list(lista[0].keys())
        encabezado = ",".join(keys) + "\n"

        archivo.write(encabezado)

        for pelicula in lista:
            values = list(pelicula.values())
            l = []
            for value in values:
                if isinstance(value,int):
                    l.append(str(value))
                elif isinstance(value,float):
                    l.append(str(value))
                else:
                    l.append(value)
            linea = ",".join(l) + "\n"
            archivo.write(linea)



#6) Ordenar películas: Se deberá mostrar por pantalla un listado de las películas ordenadas por género y dentro de las del mismo género que aparezcan ordenadas por rating descendente. 100,99,98,97

def swap_lista(lista:list, i:int, j:int)->None:
    """intercambia los valores de 2 elementos sin perderlos

    Args:
        lista (list): la lista donde estan los elementos
        i (int): el un elemento
        j (int): el otro elemento
    """
    aux = lista[i]
    lista[i] = lista[j]
    lista[j] = aux

def ordenar_peliculas_doble(peliculas:list, campo_1:str, campo_2:str, asc:bool=True):
    """ordena una lista lista en base a hasta 2 condiciones

    Args:
        peliculas (list): la lista de cosas que queres ordenar
        campo_1 (str): primer criterio por el que ordenas
        campo_2 (str): segundo criterio por el que ordenas
        asc (bool, optional): para intercambiar entre asc y desc. Defaults to True.
    """
    aux = None
    largo_lista = len(peliculas)
    for i in range(largo_lista-1):
        for j in range(i+1, largo_lista):
            if peliculas[i][campo_1] == peliculas[j][campo_1]:
                if (asc==True and peliculas[i][campo_2]>peliculas[j][campo_2]or(asc==False and peliculas[i][campo_2]<peliculas[j][campo_2])):
                    swap_lista(peliculas,i,j)

            elif (asc==True and peliculas[i][campo_1]>peliculas[j][campo_1]or(asc==False and peliculas[i][campo_1]<peliculas[j][campo_1])):
                swap_lista(peliculas,i,j)




                
# 7) Informar Mejor Rating: Mostrar el titulo y el rating de la película con más rating

def mejor_pelicula(lista:list):
    """te dice cual es la pelicula/s con mayor rating

    Args:
        lista (list): la lista con la que queres trabajar 

    Returns:
        _type_: la lista con las mejore speliculas segun el rating
    """
    bandera = True
    for peli in lista:
        if bandera == True or peli["rating"] > rating_max:
            rating_max = peli["rating"]
            bandera = False
    
    lista_mejores = []
    for peli in lista:
        if peli["rating"] == rating_max:
            lista_mejores.append(peli)
    return lista_mejores 




# 8) Guardar películas: Se deberá guardar el listado del punto anterior en un archivo JSON.

def archivo_rating(nombre_archivo:str, lista:list):
    """guarda una lista en un archivo formato json

    Args:
        nombre_archivo (str): el nombre que le quieras dar al archivo
        lista (list): la lista que quieras guardar alli
    """
    directorio_actual = os.path.dirname(__file__)
    path = os.path.join(directorio_actual, nombre_archivo)

    with open(path, mode= "w", encoding="utf-8") as archivo:
        json.dump(lista, archivo, indent=4)

