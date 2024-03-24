def matrice_in_dizionario(matrice):
    grafo = {}
    n = len(matrice)

    for i in range(n):
        adiacenze = [j for j, valore in enumerate(matrice[i]) if valore == 1]
        grafo[i] = adiacenze

    return grafo

def main():
    matrice = [[0, 1, 1], [1, 0, 1],[1, 1, 0]]

    grafo = matrice_in_dizionario(matrice)

    for nodo, adiacenze in grafo.items():
        print(f"{nodo}: {adiacenze}")

if __name__ == "__main__":
    main()