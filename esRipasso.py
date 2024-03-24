#DIZIONARIO
#dizionario = {"a":"albero", "b":"brutto", "c":"casa"}
#lista = ["albero", "brutto", "casa"]

#print(dizionario["b"])
#dizionario["d"] = "dado"
#dizionario["a"] = "asino"
#print(dizionario)
#print(lista[1])

#for chiave in dizionario:
    #print(f"(La chiave {chiave} ha valore: {dizionario[chiave]})")

#if "a" in dizionario:
    #print("a è presente nel diziionario")


#CLASSI
import random

class Nemico():
    def __init__(self, pos_x, pos_y, n_vite):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.n_vite = n_vite
    def stampa(self):
        print(f"Nemico in posizione {self.pos_x}, \
              {self.pos_y} con {self.n_vite} vite")
        
def main():
    N_NEMICI = 5
    WIDTH = 800
    HEIGHT = 400
    lista_nemici = []
    for i in range(N_NEMICI):
        pos_x = random.randint(0, WIDTH-1)
        pos_y = random.randint(0, HEIGHT-1)
        nemico = Nemico(pos_x, pos_y, 5)
        lista_nemici.append(nemico)
    print(lista_nemici)

if __name__ == "__main__":
    main()


class Personaggio():
    def __init__(self):
        pass