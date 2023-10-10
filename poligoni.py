import turtle

def disegna_poligono(lat):
    lato = 50  # Lunghezza del lato
    angolo = 360 / lat
    for _ in range(lat):
        turtle.forward(lato)
        turtle.left(angolo)

def main():
    turtle.speed(1)  # Imposta la velocità della tartaruga

    lati = [3, 4, 5, 6, 7, 8, 9, 10, 11]
    x_positions = [-100, 0, 100]  # Posizioni x delle colonne
    y_positions = [150, 50, -50]  # Posizioni y delle righe

    for y in y_positions:
        for lat in lati:
            turtle.penup()
            turtle.goto(x_positions[lati.index(lat)], y)
            turtle.pendown()
            disegna_poligono(lat)

    turtle.done()

if __name__ == "__main__":
    main()

