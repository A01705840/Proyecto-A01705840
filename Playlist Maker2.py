"""
Proyecto Creador de Playlists
El programa reliza una búsqueda de artísta
y pone en una playlist, las canciones más famosas.
Se pueden retirar y añadir canciones.
"""
#La Bilbioteca que usaré más tarde se llama Spotipy.
#tuve que registrarme como desarrolladora para tener un cliend ID y usar la biblioteca
#Con la biblioteca, quiero poner más artistas y canciones y hacer playlist de Spotify
play_list = [ ]
lista_artistas = ["Imagine Dragons" , "Harry Styles", "Alejandro Fernández",\
    "Kishi Bashi", "Hans Zimmer", "Lorde"]
print("Hola! Hagamos tu nueva playlist!")
print("Escoge tres artistas: ")
print ("{:<8}".format('Artistas'))

for v in lista_artistas:
    Artistas = v
    print ("{:<8}".format(Artistas)) #Para que se vea en forma de lista #Formato Tabular de DelftStack(2021)Imprimir datos en formato tabular en Python


artista_1 = str(input("Dime tu artista favorito: "))
artista_2 = str(input("Dime otro artista famoso: "))
artista_3 = str(input("Dime tu último artista: "))
def busca_canciones(artista_1, artista_2, artista_3):
    global play_list
    while len(play_list) < 15:
        if artista_1  == "Imagine Dragons" or artista_2   == "Imagine Dragons" or artista_3  == "Imagine Dragons" \
           or "imagine dragons":
            play_list.append("Believer")
            play_list.append("Thunder")
            play_list.append("Natural")
            play_list.append("Whatever It Takes")
            play_list.append("Radioactive")
        if artista_1 == "Harry Styles" or artista_2 == "Harry Styles" or artista_3  == "Harry Styles" or "harry styles":
            play_list.append("Adore You")
            play_list.append("Falling")
            play_list.append("Lights Up")
            play_list.append("Sign of Times")
            play_list.append("Watermelon Sugar")
        if artista_1 == "Alejandro Fernandez" or artista_2 == "Alejandro Fernandez"  or artista_3 == "Alejandro Fernandez"\
           or "alejandro fenandez":
            play_list.append("Amor de los Dos")
            play_list.append("No")
            play_list.append("Nube Viajera")
            play_list.append("Abrázame")
            play_list.append("Mátalas")
        if artista_1 == "Kishi Bashi" or artista_2 == "Kishi Bashi" or artista_3 == "Kishi Bashi"\
           or "kishi bashi":
            play_list.append("I am the Anti-Christ to you")
            play_list.append("Honeybody")
            play_list.append("This Must Be The Place")
            play_list.append("Can`t let go Juno")
            play_list.append("Bright Whites")
        if artista_1  == "Hans Zimmer" or artista_2  == "Hans Zimmer" or artista_3 == "Hans Zimmer"\
           or "hans zimmer":
            play_list.append("Cornfield Chase")
            play_list.append("Time")
            play_list.append("Main Titles: Top Gun Maverick")
            play_list.append("Day One")
            play_list.append("Darkstar")
        if artista_1  == "Lorde" or artista_2  == "Lorde" or artista_3 == "Lorde"\
           or "lorde":
            play_list.append("Ribs")
            play_list.append("Royals")
            play_list.append("Team")
            play_list.append("Liability")
            play_list.append("Green Light")
        else:
            print("Lo siento, no hay datos del artista :(")
    return play_list

def nueva_playlist(nueva_canc):
    play_list.append(nueva_canc)
    return play_list

def quitar_cancion(no_canc):
    play_list.remove(no_canc)
    return play_list
 
busca_canciones(artista_1, artista_2, artista_3)
print("{:<8}".format('Canciones'))

for v in play_list:
    Canciones = v
    print ("{:<8}".format(Canciones))
    
while True:    #Junté las funciones de añadir y quitar canciones en solo una pregunta
    print("¿Añadir otra canción? - A")
    print("¿Quitar una canción?-Q")
    print("Si deseas salir: - Exit")
    add_canc = input()
    if add_canc == "A" or add_canc == "a":
        nueva_canc = input("Escribe canción: ")
        print("Tu nueva playlist es ")
        nueva_playlist(nueva_canc)
        print("{:<8}".format('Canciones'))
        
        for v in play_list:
            Canciones = v
            print ("{:<8}".format(Canciones))
        continue
    elif add_canc == "Q" or add_canc == "q":
        no_canc = input("¿Cuál canción? ")
        print("Tu nueva playlist es: ")
        quitar_cancion(no_canc)
        print("{:<8}".format('Canciones'))

        for v in play_list:
            Canciones = v
            print ("{:<8}".format(Canciones))
        continue
    else:
        print("OK")
        break