import turtle

def print_list(l):
    print("\nLa lista è:", end=" ")
    for elemento in l:
        print(elemento, end=" ")
    print("\n")

def main():
    comandi = []
    comando = 0
    while comando != -1:
        comando = int(input("Inserisci un comando (-1 per terminare):\n"
                            "1: Avanti\n"
                            "2: Girare a destra\n"
                            "3: Girare a sinistra\n"))
        if comando == -1:
            break
        if comando != 1 and comando != 2 and comando != 3:
            print("Comando non valido.")
            continue
        valore = int(input("Inserisci il valore per il comando: "))
        comandi.append((comando, valore))

    print_list(comandi)
    
    turtle.speed(1)  # Imposta la velocità della turtle
    for comando, valore in comandi:
        if comando == 1:
            turtle.forward(valore)
        elif comando == 2:
            turtle.right(valore)
        elif comando == 3:
            turtle.left(valore)

    turtle.done()  # Chiudi la finestra alla fine dell'esecuzione

if __name__ == "__main__":
    main()

