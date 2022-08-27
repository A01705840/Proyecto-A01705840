"""
Proyecto Creador de Playlists
El programa reliza una búsqueda de artísta
y pone en una playlist, las canciones más famosas.
Se pueden retirar y añadir canciones.
"""
#En está semana, intenté descargar una biblioteca de música
#de Spotify para developers. Pero no logré implementarla.
#Por lo que, por el momento solo incluyo algunos artistas y canciones
#para correr el programa.
print("Hola! Hagamos tu nueva playlist!")
artista_1 = str(input("Dime tu artista favorito: "))
artista_2 = str(input("Dime otro artista famosos: "))
artista_3 = str(input("Dime tu último artista: "))

list = play_list = []
list = lista_artistas = ["Imagine Dragons", "Harry Styles", "Alejandro Fernández", "Kishi Bashi", "Hans Zimmer", "Lorde"]
def busca_canciones(artista_1, artista_2, artista_3):
    global play_list
    while len(play_list) < 15:
        if artista_1 and artista_2 and artista_3 in lista_artistas:
#Intenté hacer la condición de los artistas como or, pero solo se repetían las mismas canciones.
#Decidí mejor hacer para cada variable de artista su propia condición.
            if artista_1 == "Imagine Dragons":
                play_list.append("Believer")
                play_list.append("Thunder")
                play_list.append("Natural")
                play_list.append("Whatever It Takes")
                play_list.append("Radioactive")
            elif artista_1 =="Harry Styles":
                play_list.append("Adore You")
                play_list.append("Falling")
                play_list.append("Lights Up")
                play_list.append("Sign of Times")
                play_list.append("Watermelon Sugar")
            elif artista_1 =="Alejandro Fernandez":
                play_list.append("Amor de los Dos")
                play_list.append("No")
                play_list.append("Nube Viajera")
                play_list.append("Abrázame")
                play_list.append("Mátalas")
            elif artista_1 =="Kishi Bashi":
                play_list.append("I am the Anti-Christ to you")
                play_list.append("Honeybody")
                play_list.append("This Must Be The Place")
                play_list.append("Can`t let go Juno")
                play_list.append("Bright Whites")
            elif artista_1 == "Hanz Zimmer":
                play_list.append("Cornfield Chase")
                play_list.append("Time")
                play_list.append("Main Titles: Top Gun Maverick")
                play_list.append("Day One")
                play_list.append("Darkstar")
            elif artista_1 == "Lorde":
                play_list.append("Ribs")
                play_list.append("Royals")
                play_list.append("Team")
                play_list.append("Liability")
                play_list.append("Green Light")
            elif artista_2 == "Imagine Dragons" and len(play_list) < 10:
                play_list.append("Believer")
                play_list.append("Thunder")
                play_list.append("Natural")
                play_list.append("Whatever It Takes")
                play_list.append("Radioactive")
            elif artista_2 =="Harry Styles" and len(play_list) < 10:
                play_list.append("Adore You")
                play_list.append("Falling")
                play_list.append("Lights Up")
                play_list.append("Sign of Times")
                play_list.append("Watermelon Sugar")
            elif artista_2 =="Alejandro Fernandez" and len(play_list) < 10:
                play_list.append("Amor de los Dos")
                play_list.append("No")
                play_list.append("Nube Viajera")
                play_list.append("Abrázame")
                play_list.append("Mátalas")
            elif artista_2 =="Kishi Bashi" and len(play_list) < 10:
                play_list.append("I am the Anti-Christ to you")
                play_list.append("Honeybody")
                play_list.append("This Must Be The Place")
                play_list.append("Can`t let go Juno")
                play_list.append("Bright Whites")
            elif artista_2 == "Hanz Zimmer"  and len(play_list) < 10:
                play_list.append("Cornfield Chase")
                play_list.append("Time")
                play_list.append("Main Titles: Top Gun Maverick")
                play_list.append("Day One")
                play_list.append("Darkstar")
            elif artista_2 == "Lorde" and len(play_list) < 10:
                play_list.append("Ribs")
                play_list.append("Royals")
                play_list.append("Team")
                play_list.append("Liability")
                play_list.append("Green Light")
            elif artista_3 == "Imagine Dragons" and len(play_list) < 15:
                play_list.append("Believer")
                play_list.append("Thunder")
                play_list.append("Natural")
                play_list.append("Whatever It Takes")
                play_list.append("Radioactive")
            elif artista_3 =="Harry Styles" and len(play_list) < 15:
                play_list.append("Adore You")
                play_list.append("Falling")
                play_list.append("Lights Up")
                play_list.append("Sign of Times")
                play_list.append("Watermelon Sugar")
            elif artista_3 =="Alejandro Fernandez" and len(play_list) < 15:
                play_list.append("Amor de los Dos")
                play_list.append("No")
                play_list.append("Nube Viajera")
                play_list.append("Abrázame")
                play_list.append("Mátalas")
            elif artista_3 =="Kishi Bashi" and len(play_list) < 15:
                play_list.append("I am the Anti-Christ to you")
                play_list.append("Honeybody")
                play_list.append("This Must Be The Place")
                play_list.append("Can`t let go Juno")
                play_list.append("Bright Whites")
            elif artista_3 == "Hanz Zimmer" and len(play_list) < 15:
                play_list.append("Cornfield Chase")
                play_list.append("Time")
                play_list.append("Main Titles: Top Gun Maverick")
                play_list.append("Day One")
                play_list.append("Darkstar")
            elif artista_3 == "Lorde" and len(play_list) < 15:
                play_list.append("Ribs")
                play_list.append("Royals")
                play_list.append("Team")
                play_list.append("Liability")
                play_list.append("Green Light")
            else:
                print("Lo siento, no hay datos del artista :(")
        else:
            print("Lo siento, no hay datos del artista :(")
    return play_list

def nueva_playlist(nueva_canc):
    play_list.append(nueva_canc)
    return play_list
def quitar_cancion(no_canc):
    play_list.remove(no_canc)
    return play_list
print("Aqui esta tu nueva playlist! ", busca_canciones(artista_1,artista_2,artista_3))
add_canc = str(input("¿Añadir otra canción?(y/n) "))
if add_canc == "y":
    nueva_canc = input("Escribe canción: ")
    print("Tu nueva playlist es ", nueva_playlist(nueva_canc))
else:
    print("ok")
quit_canc = str(input("¿Retirar una canción?(y/n)"))
if quit_canc == "y":
    no_canc = input("¿Cuál canción?")
    print("Tu nueva playlist es ", quitar_cancion(no_canc))
else:
    print("ok")