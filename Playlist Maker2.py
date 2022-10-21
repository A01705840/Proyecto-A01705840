
from time import sleep
import sys
"""
Proyecto Creador de Playlists
El programa reliza una búsqueda de artísta
y pone en una playlist, las canciones más famosas.
Se pueden retirar y añadir canciones.
"""

'''--------------------------CREACIÓN DE PLAYLIST-------------------------'''


def text(texto, speed):
    """
    (uso de biblioteca, uso de funciones)
    recibe: string de texto,velocidad de texto
    imprime cada letra segun la velocidad
    devuelve: texto impreso según la velocidad
    """
    for c in texto:
        print(c, end='')
        sys.stdout.flush()
        sleep(speed)


def busca_canciones(artista_1, artista_2, artista_3, play_list):
    """
   (uso de condiciones, uso de funciones)
   recibe: asrtista_1, artista_2, artista_3 (cadena) y play_list (lista)
   busca los tres artistas y añade las top 5 canciones a la lista play_list
   devuelve: playlist con las top 5 canciones de los 3 artistas
   """
    while len(play_list) < 15:
        if artista_1 == "Harry Styles" or artista_1 == "harry styles" or\
                artista_2 == "Harry Styles" or artista_2 == \
                "harry styles" or artista_3 == "Harry Styles"\
                or artista_3 == "harry styles":
            play_list.extend(["Adore You", "Falling", "Lights Up",
                              "Sign of Times", "Watermelon Sugar"])
        if artista_1 == "Imagine Dragons" or artista_1 == "imagine dragons"\
                or artista_2 == "Imagine Dragons" or artista_2 ==\
                "imagine dragons" or artista_3 == "Imagine Dragons" or\
                artista_3 == "imagine dragons":
            play_list.extend(["Believer", "Thunder", "Natural",
                              "Whatever It Takes", "Radioactive"])
        if artista_1 == "Alejandro Fernandez" or artista_1 == \
                "alejandro fernandez" or artista_2 ==\
                "Alejandro Fernandez" or artista_2 ==\
                "alejandro fernandez" or artista_3 == \
                "Alejandro Fernandez" or artista_3 == \
                "alejandro fernandez":
            play_list.extend(["Amor de los Dos", "No", "Nube Viajera",
                              "Abrázame", "Mátalas"])
        if artista_1 == "Kishi Bashi" or artista_1 == "kishi bashi" or\
                artista_2 == "Kishi Bashi" or artista_2 == "kishi bashi"\
                or artista_3 == "Kishi Bashi"\
                or artista_3 == "kishi bashi":
            play_list.extend(["I am the Anti-Christ to you", "Honeybody",
                              "This Must Be The Place", "Can't let go Juno",
                              "Bright Whites"])
        if artista_1 == "Hans Zimmer" or artista_1 == "hans zimmer" or \
                        artista_2 == "Hans Zimmer" or artista_2 == \
                        "hans zimmer" or artista_3 == "Hans Zimmer" or \
                        artista_3 == "hans zimmer":
            play_list.extend(
                ["Cornfield Chase", "Time", "Main Titles: Top Gun Maverick",
                 "Day One", "Darkstar"])
        if artista_1 == "Lorde" or artista_1 == "lorde" or artista_2 ==\
                        "Lorde" or artista_2 == "lorde" or artista_3 ==\
                        "Lorde" or artista_3 == "lorde":
            play_list.extend(["Ribs", "Royals", "Team", "Liability",
                              "Green Light"])
        else:
            print("Lo siento, no hay datos del artista :(")


def nueva_cancion(nueva_canc):
    """
   (uso de ciclos for, uso de funciones)
   recibe: nueva_canc (cadena), nombre de la nueva canción
   devuelve: la playlist con las canciones previamente añadidas
   y la nueva canción
   """
    play_list.append(nueva_canc)
    for v in play_list:
        Canciones = v
        print("{:<8}".format(Canciones))


def quitar_cancion(no_canc):
    """
    (uso de ciclos for,  uso de condicionales, uso de funciones)
    recibe: no_canc (cadena), nombre de la canción que se quiere eliminar
    Se busca y borra el nombre de la canción y se quita de la lista play_list.
    Si no se encuentra se avisa al usuario.
    devuelve: la playlist con las canciones previamente añadidas, pero sin la
    canción eliminada
    """
    if no_canc in play_list:
        play_list.remove(no_canc)
        for v in play_list:
            Canciones = v
            print("{:<8}".format(Canciones))
    else:
        print("La canción no está en esta playlist")


'''----------------------------VER ARTISTAS-------------------------------'''


def obten_lista_de_artista(lista_artistas, art_canc):
    """
    (uso de ciclos for,  uso de condicionales, uso de funciones)
    recibe: lista (lista)
    devuelve: la playlist con las canciones previamente añadidas,
    pero sin la canción eliminada
    """
    art_canc = input("Escoge un artista para ver sus canciones:")
    for linea in lista_artistas:
        if art_canc == linea[0]:
            linea.pop(0)
            print(linea)


'''----Listas y variables-----'''
lista_artistas = [
    ["Imagine Dragons", "Believer", "Thunder",
        "Natural", "Whatever It Takes", "Radioactive"],
    ["Harry Styles", "Adore You", "Falling", "Lights Up",
        "Sign of Times", "Watermelon Sugar"],
    ["Alejandro Fernández", "Amor de los Dos", "No",
        "Nube Viajera", "Abrázame", "Mátalas"],
    ["Kishi Bashi", "I am the Anti-Christ to you", "Honeybody",
        "This Must Be The Place", "Can't let go Juno", "Bright Whites"],
    ["Hans Zimmer", "Cornfield Chase", "Time",
        "Main Titles: Top Gun Maverick", "Day One", "Darkstar"],
    ["Lorde", "Ribs", "Royals", "Team", "Liability", "Green Light"]]
play_list = []
artista_1 = str
artista_2 = str
artista_3 = str
add_canc = str
''''--------------------------INICIO DE PROGRAMA--------------------------'''
print("Hola! Hagamos tu nueva playlist!")
print("Escoge tres artistas: ")
print("{:<8}".format('Artistas'))
i = 0
while i < len(lista_artistas):
    Artistas = lista_artistas[i][0]
    print(Artistas)
    i = i + 1

'''---Escoger Artistas---'''
artista_1 = str(input("Dime tu artista favorito: "))
artista_2 = str(input("Dime otro artista famoso: "))
artista_3 = str(input("Dime tu último artista: "))


busca_canciones(artista_1, artista_2, artista_3, play_list)
for v in play_list:
    Canciones = v
    print("{:<8}".format(Canciones))

'''----Menú de opciones----'''
a = ("¿Añadir otra canción? - A\n")
q = ("¿Quitar una canción?-Q\n")
v = ("Volver a ver los artistas - V\n")
e = ("Si deseas salir: - Exit\n")
text(a, 0.03)
text(q, 0.03)
text(v, 0.03)
text(e, 0.03)
add_canc = input()


while add_canc != "Exit" and add_canc != "exit":
    if add_canc == "A" or add_canc == "a":
        nueva_canc = input("Escribe canción: ")
        print("Tu nueva playlist es: ")
        nueva_cancion(nueva_canc)
        add_canc = "%"
    if add_canc == "Q" or add_canc == "q":
        no_canc = input("¿Cuál canción? ")
        print("Tu nueva playlist es: ")
        quitar_cancion(no_canc)
        add_canc = "%"
    if add_canc == "V" or add_canc == "v":
        i = 0
        while i < len(lista_artistas):
            Artistas = lista_artistas[i][0]
            print(Artistas)
            i = i + 1
        art_canc = " "
        obten_lista_de_artista(art_canc, lista_artistas)
        add_canc = "%"
    if add_canc == "%":
        print("¿Añadir otra canción? - A")
        print("¿Quitar una canción?-Q")
        print("Volver a ver los artistas - V")
        print("Si deseas salir: - Exit")
        add_canc = input()
    else:
        print("Por favor, ingrese una de las tres opciones")
        add_canc = "%"
