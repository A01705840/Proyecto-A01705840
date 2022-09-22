
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
        if artista_1  == "Imagine Dragons" or "imagine dragons" or artista_2   == "Imagine Dragons" or "imagine dragons" or artista_3  == "Imagine Dragons"\
        or artista_3  =="imagine dragons":
            play_list.extend(["Believer","Thunder","Natural","Whatever It Takes", "Radioactive"])
        if artista_1 == "Harry Styles"   or artista_1 == "harry styles"or artista_2 == "Harry Styles"  or artista_2 == "harry styles" or artista_3 == "Harry Styles"\
        or artista_3 =="harry styles":
            play_list.extend(["Adore You","Falling","Lights Up","Sign of Times", "Watermelon Sugar"])
        if artista_1 == "Alejandro Fernandez"   or artista_1 == "alejandro fernandez"or artista_2 == "Alejandro Fernandez"\
        or artista_2 == "alejandro fernandez" or artista_3 == "Alejandro Fernandez" or artista_3 =="alejandro fernandez":
            play_list.extend(["Amor de los Dos", "No", "Nube Viajera", "Abrázame", "Mátalas"])
        if artista_1 == "Kishi Bashi" or artista_1 == "kishi bashi"or artista_2 == "Kishi Bashi" or artista_2 == "kishi bashi" or artista_3 == "Kishi Bashi"\
        or artista_3 == "kishi bashi":
            play_list.extend(["I am the Anti-Christ to you", "Honeybody", "This Must Be The Place","Can't let go Juno","Bright Whites"])
        if artista_1  == "Hans Zimmer" or artista_1  == "hans zimmer" or artista_2  == "Hans Zimmer" or artista_2  == "hans zimmer" or artista_3 == "Hans Zimmer"\
        or artista_3  == "hans zimmer":
            play_list.extend(["Cornfield Chase", "Time", "Main Titles: Top Gun Maverick", "Day One", "Darkstar"])
        if artista_1  == "Lorde"  or artista_1  == "lorde" or artista_2  == "Lorde"  or artista_2  == "lorde" or artista_3 ==  "Lorde"\
        or artista_3  == "lorde":
            play_list.extend(["Ribs", "Royals", "Team","Liability","Green Light"])
        else:
            print("Lo siento, no hay datos del artista :(")

def nueva_playlist(nueva_canc):
    global play_list
    play_list.append(nueva_canc)
    for v in play_list:
            Canciones = v
            print("{:<8}".format(Canciones))
    add_canc = "%"
def quitar_cancion(no_canc):
    global play_list
    if no_canc in play_list:
        play_list.remove(no_canc)
        for v in play_list:
                Canciones = v
                print("{:<8}".format(Canciones))
    else:
        print("La canción no está en esta playlist")
    
busca_canciones(artista_1, artista_2, artista_3)
for v in play_list:
    Canciones = v
    print ("{:<8}".format(Canciones))
    
print("¿Añadir otra canción? - A")
print("¿Quitar una canción?-Q")
print("Si deseas salir: - Exit")
add_canc = input()

while add_canc != "Exit" and add_canc != "exit": #Cambié el while True con break al final por un while que terminara con la palabra Exit. 
    if add_canc == "A" or add_canc == "a":
        nueva_canc = input("Escribe canción: ")
        print("Tu nueva playlist es: ")
        nueva_playlist(nueva_canc)
        add_canc = "%"
    if add_canc == "Q" or add_canc == "q":
        no_canc = input("¿Cuál canción? ")
        print("Tu nueva playlist es: ")
        quitar_cancion(no_canc)
        add_canc = "%"
    if add_canc == "%":
        print("¿Añadir otra canción? - A")
        print("¿Quitar una canción?-Q")
        print("Si deseas salir: - Exit")
        add_canc = input()
    else:
        print("Por favor, ingrese una de las tres opciones")
        add_canc = "%"