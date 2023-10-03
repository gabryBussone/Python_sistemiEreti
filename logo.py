import turtle #esempio di importazione di un modulo built - in

n = int(input("inserisci il nunero di lati: "))
lato = int(input("inserisci la lunghezza del lato: "))

finestra = turtle.Screen() #creazione finestra
alice = turtle.Turtle() #creazione tartaruga (cursore)

# Cambia il colore della freccia
alice.color("green")  # Puoi sostituire "red" con il colore desiderato

angolo = 360 / n

alice.speed(1000)

# Inizia il riempimento del poligono chiuso
alice.begin_fill()

for i in range(n):
    alice.forward(lato) #va avanti di 100 
    alice.left(angolo)

alice.color("red")

# Termina il riempimento del poligono chiuso
alice.end_fill()

finestra.mainloop() #gestione finestra


