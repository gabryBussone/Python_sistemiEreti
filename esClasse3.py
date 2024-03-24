import turtle

def main():
    def disegna_maglia_quadra(lato):
        for _ in range(4):
            turtle.forward(lato)
            turtle.right(90)

    def disegna_griglia(rows, cols, lato):
        for _ in range(rows):
            for _ in range(cols):
                disegna_maglia_quadra(lato)
                turtle.forward(lato)
            turtle.backward(lato * cols)
            turtle.right(90)
            turtle.forward(lato)
            turtle.left(90)

    lato_maglia = 10
    righe = 4
    colonne = 4

    turtle.speed(2)

    disegna_griglia(righe, colonne, lato_maglia)

if __name__ == "__main__":
    main()



