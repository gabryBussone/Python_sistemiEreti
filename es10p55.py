def main():
    # Assegna i voti a una lista
    lista_voti = [8, 7, 9, 6, 8, 10, 7]

    # Stampa la lista senza il primo e l'ultimo voto
    print("Lista senza il primo e l'ultimo voto:")
    print(lista_voti[1:-1])

    # Sostituisci il quarto voto con un 10
    lista_voti[3] = 10

    # Stampa i primi 3 voti della lista
    print("Primi 3 voti della lista:")
    print(lista_voti[:3])

if __name__ == "__main__":
    main()
