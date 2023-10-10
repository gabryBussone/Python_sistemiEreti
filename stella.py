import turtle

# inserisic il numero di punte
n = int(input("Inserisci il numero di punte della stella: "))

# inserisci la lunghezza del lato
lunghezza_lato = float(input("Inserisci la lunghezza del lato della stella: "))

finestra = turtle.Screen() #creazione finestra

# cambia il colore della freccia
turtle.color("black")  # Puoi sostituire "red" con il colore desiderato

# velocità della turtle
turtle.speed("slow")

# calcolo angoloe
angolo = 360 / n

# inizia il riempimento del poligono chiuso
turtle.begin_fill()

# disegno stella
for i in range(n):
    turtle.forward(lunghezza_lato)  # disegna punte
    turtle.right(angolo)  # angolo da girare
    turtle.forward(lunghezza_lato)  # disegna lati parte interna
    turtle.left(2 * angolo)  # angolo da girare

turtle.color("yellow")

# termina il riempimento del poligono chiuso
turtle.end_fill()

finestra.mainloop() #gestione finestra
