import turtle

def sopra():
    turtle.setheading(90)
    turtle.forward(50)

def sotto():
    turtle.setheading(270)
    turtle.forward(50)

def destra():
    turtle.setheading(0)
    turtle.forward(50)

def sinistra():
    turtle.setheading(180)
    turtle.forward(50)

def main():
    turtle.speed(1)

    while True:
        dizionario = {"su": sopra, "giu": sotto, "dx": destra, "sx": sinistra}
        direzione = input("Inserisci una direzione (su, giu, dx, sx) o 'esci' per uscire: ")

        if direzione == 'a':

        if direzione in dizionario:
            dizionario[direzione]() 
        else:
            print("Errore")

    turtle.done()

if __name__ == "__main__":
    main()

