#disegno la matrice a partire dal dizionario
def pratty_print(matrice, separatore = "\t"):
    for riga in matrice:
        riga_str = [str(x) for x in riga]
        print(separatore.join(riga_str))

def main():
    grafo = {0: [1, 2], 1: [0, 2], 2: [0, 1]}
    n = len(grafo)
    matrice = [[0] * n for _ in range(n)]

    for k,v in grafo.items():
        for h in v:
            matrice[k][h] = 1
    
    pratty_print(matrice, " ")
    
if __name__ == "__main__":
    main()
