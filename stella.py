import turtle

# Ottieni il numero di punte dalla tastiera
n = int(input("Inserisci il numero di punte della stella: "))

# Ottieni la lunghezza del lato dalla tastiera
lunghezza_lato = float(input("Inserisci la lunghezza del lato della stella: "))

# Impostazioni iniziali della tartaruga
turtle.speed(1)

# Calcola l'angolo tra le punte della stella
angolo = 360 / n

# Disegna la stella
for _ in range(n):
    turtle.forward(lunghezza_lato)  # Lunghezza delle punte della stella
    turtle.right(180 - angolo)
    turtle.forward(lunghezza_lato)  # Lunghezza della parte interna della stella
    turtle.left(180 - angolo)

# Chiudi la finestra quando si fa clic su di essa
turtle.exitonclick()



