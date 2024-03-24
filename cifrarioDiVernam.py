#fare una classe testo le cui istante possano contenere sia un testo chiaro sia un testo codificato

class Testo:
    def __init__(self, testo_chiaro="", chiave=""):
        self.testo_chiaro = testo_chiaro
        self.chiave = chiave
        self.testo_codificato = self.cifratura_vernam() != ""

    def cifratura_vernam(self):
        if not self.chiave:
            print("Errore: La chiave è necessaria per la cifratura di Vernam")
            return ""

        lettere_a_numeri = {}
        numeri_a_lettere = {}
        alphabet = "abcdefghijklmnopqrstuvwxyz"

        for i in range(26):
            lettere_a_numeri[alphabet[i]] = str(i)
            numeri_a_lettere[str(i)] = alphabet[i]

        numeri_testo = [lettere_a_numeri[carattere] for carattere in self.testo_chiaro.lower() if carattere.isalpha()]
        numeri_chiave = [lettere_a_numeri[carattere] for carattere in self.chiave.lower() if carattere.isalpha()]

        numeri_cifrati = [(int(num_testo) ^ int(num_chiave)) for num_testo, num_chiave in zip(numeri_testo, numeri_chiave * (len(numeri_testo) // len(numeri_chiave) + 1))]

        cifrato = ''.join([numeri_a_lettere[str(numero)] for numero in numeri_cifrati])

        return cifrato

testo_in_chiaro = input("Inserisci il testo in chiaro: ")
chiave = input("Inserisci la chiave: ")

testo = Testo(testo_in_chiaro, chiave)

print("Testo in chiaro:", testo.testo_chiaro)
print("Chiave:", testo.chiave)
print("Testo codificato:", testo.testo_codificato)






