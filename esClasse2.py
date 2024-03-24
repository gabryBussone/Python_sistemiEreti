import random

def main():

    def movimento_casuale():
        return random.choice([-1, 1])

    def genera_spostamenti_casuali(giorni, movimenti_al_secondo):
        totale_movimenti = giorni * 24 * 60 * 60
        spostamenti_casuali = [movimento_casuale() for _ in range(totale_movimenti)]
        return spostamenti_casuali

    def calcola_spostamento_complessivo(spostamenti_casuali):
        spostamento_complessivo = 0
        for spostamento in spostamenti_casuali:
            spostamento_complessivo += spostamento
        return spostamento_complessivo

    spostamenti_casuali = genera_spostamenti_casuali(5, 1)

    spostamento_complessivo = calcola_spostamento_complessivo(spostamenti_casuali)

    print(f"Spostamento complessivo dopo 5 giorni: {spostamento_complessivo} cm")

if __name__ == "__main__":
    main()