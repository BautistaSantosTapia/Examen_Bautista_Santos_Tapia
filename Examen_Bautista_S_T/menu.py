
# Requerimientos del desarrollo.
# Nota 1: Todas las funciones deben estar en un módulo distinto al programa principal
# y respetar las reglas de estilo de la cátedra.
# Nota 2: Todas las funciones deben tener su propio docstring
# Nota 3: Para ordenar se deberá utilizar los algoritmos de ordenamiento vistos en la catedra
"""Enunciado:
Se dispone de un archivo con datos acerca de películas, que tiene el siguiente formato:
id_peli, titulo, genero, rating
por ejemplo: 1,Adventures of Rocky,sin genero,0
2,My Brother the Devil,sin genero,0
3,Criminal,sin genero,0
Se deberá realizar un programa que permita el análisis de dicho archivo y sea capaz de generar
nuevos archivos de salida de formato similar filtrados por varios criterios:
el programa contará con el siguiente menú:
1) Cargar archivo .CSV: Se pedirá el nombre del archivo y se cargará en una lista de diccionarios los elementos del mismo.
2) Imprimir lista: Se imprimirá por pantalla la tabla con los datos de las películas.
3) Asignar rating: Se deberá hacer uso de la función map. La cual recibirá la lista y una
función que asignará a la película un valor de rating flotante entre 1 y 10 con 1 decimal
calculado de manera aleatoria se mostrará por pantalla el mismo.
4) Asignar género: Se deberá hacer uso de la función map. La cual recibirá la lista y una
función que asignará a la película un género de acuerdo a un número aleatorio entre 1 y 4.
1: drama
2: comedia
3: acción
4: terror
5) Filtrar por género: Se deberá pedir un género y escribir un archivo igual al original, pero
donde solo
aparezcan películas del género seleccionado. El nombre del archivo será p.e. comedias.csv
6) Ordenar películas: Se deberá mostrar por pantalla un listado de las películas ordenadas por
género y dentro de las del mismo género que aparezcan ordenadas por rating descendente.
7) Informar Mejor Rating: Mostrar el titulo y el rating de la película con más rating
8) Guardar películas: Se deberá guardar el listado del punto anterior en un archivo JSON.
9) Salir."""

from funciones import *
bandera_1 = True
bandera_2 = True
bandera_3 = True
bandera_4 = True
bandera_5 = True
bandera_6 = True
bandera_7 = True

while True:
    match menu():
        case "1":
            cargar_archivo_csv("movies.csv")
            bandera_1 = False

        case "2":
            if bandera_1 == False:
                lista_peliculas = cargar_archivo_csv("movies.csv")
                mostrar_lista(lista_peliculas)
                
                bandera_2 = False
            else:
                print("Primero tener que seleccionar la opcion de arriba")

        case "3":
            if bandera_2 == False:
                asignar_rating(lista_peliculas)
                mostrar_lista(lista_peliculas)
                bandera_3 = False
            else:
                print("Primero tener que seleccionar la opcion de arriba")

        case "4":
            if bandera_3 == False:
                generos = ["drama","comedia","acción","terror"]
                asignar_genero(lista_peliculas,generos)
                mostrar_lista(lista_peliculas)
                bandera_4 = False
            else:
                print("Primero tener que seleccionar la opcion de arriba")

        case "5":
            if bandera_4 == False:
                genero_elegido = input("Ingrese genero: ")
                lista_generos = pelicula_genero(lista_peliculas,genero_elegido)
                mostrar_lista(lista_generos)
                archivo_genero("genero.csv",lista_generos)  
                bandera_5 = False
            else:
                print("Primero tener que seleccionar la opcion de arriba")

        case "6":
            if bandera_5 == False:
                ordenar_peliculas_doble(lista_peliculas,"genero","rating",False)
                mostrar_lista(lista_peliculas)            
                bandera_6 = False
            else:
                print("Primero tener que seleccionar la opcion de arriba")

        case "7":
            if bandera_6 == False:
                lista_mejor_ranking = mejor_pelicula(lista_peliculas)

                for peli in lista_mejor_ranking:
                    print(f'{peli["titulo"]:<30} {peli["rating"]:4.1f}')
                bandera_7 = False
            else:
                print("Primero tener que seleccionar la opcion de arriba")

        case "8":
            if bandera_7 == False:
                archivo_rating("rating.json",lista_mejor_ranking)
            else:
                print("Primero tener que seleccionar la opcion de arriba")

        case "9":
                respuesta = input("Queres salir (s/n)? ").lower()
                if respuesta == "s":
                    break
                else:
                    continue
    pausar()

print("Fin del programa")





