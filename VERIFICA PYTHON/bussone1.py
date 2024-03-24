#ANALISI DEL TESTO

class Testo:
    def __init__(self, testo):

        self.testo = testo

    def numero_caratteri(self):

        return len(self.testo)

    def lista_parole(self):

        return self.testo.split()

    def lista_lunghezze(self):

        parole = self.lista_parole()
        return [len(parole) for parole in parole]

    def cerca_parola(self, parole):
        print

    def salva_su_file(self, nome_file):

        with open(nome_file, 'w') as file:
            file.write(self.testo)

    def frequenza_parole(parole):

        frequenza = {}
        for parola in parole:
            if parola in frequenza:
                frequenza[parola] += 1
            else:
                frequenza[parola] = 1
        return frequenza


def main():

    testo = Testo("ciao sono gabriel e sono uno studente dell'ITIS mario delpozzo")

    print("numero di caratteri: ", testo.numero_caratteri())

    print("lista delle parole: ", testo.lista_parole())

    print("lista delle lunghezze delle parole del testo: ", testo.lista_lunghezze())

    testo.salva_su_file("testo.txt")

    parole = testo.lista_parole()
    frequenza = Testo.frequenza_parole(parole)
    print("dizionario con all'interno la frequenza delle parole:")
    for parola, ix in frequenza.items():
        print(parola, ":", i)

if __name__ == "__main__":
    main()




