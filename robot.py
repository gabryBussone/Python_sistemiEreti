import pygame
import csv

BIANCO = (255, 255, 255)
NERO = (0, 0, 0)
ROSSO = (255, 0, 0)

def carica_griglia_da_csv(nome_file):
    griglia = []
    with open(nome_file, 'r') as file:
        lettore = csv.reader(file)
        for riga in lettore:
            griglia.append(list(map(int, riga)))
    return griglia

def trova_percorso(griglia):
    percorso = []
    for y, riga in enumerate(griglia):
        for x, cella in enumerate(riga):
            if cella == 0:
                percorso.append((x, y))
    return percorso

def disegna_griglia(schermo, griglia, dimensione_cella):
    for y, riga in enumerate(griglia):
        for x, cella in enumerate(riga):
            colore = BIANCO if cella == 0 else NERO
            pygame.draw.rect(schermo, colore, (x * dimensione_cella, y * dimensione_cella, dimensione_cella, dimensione_cella))
            pygame.draw.rect(schermo, NERO, (x * dimensione_cella, y * dimensione_cella, dimensione_cella, dimensione_cella), 1)

def disegna_percorso(schermo, percorso, dimensione_cella):
    for nodo in percorso:
        pygame.draw.rect(schermo, ROSSO, (nodo[0] * dimensione_cella, nodo[1] * dimensione_cella, dimensione_cella, dimensione_cella))

def main():
    nome_file_griglia = "mappa.csv"
    dimensione_griglia = 4
    dimensione_cella = 50 
    larghezza_schermo = dimensione_griglia * dimensione_cella
    altezza_schermo = dimensione_griglia * dimensione_cella

    pygame.init()
    schermo = pygame.display.set_mode((larghezza_schermo, altezza_schermo))

    griglia = carica_griglia_da_csv(nome_file_griglia)

    percorso = trova_percorso(griglia)

    in_esecuzione = True
    while in_esecuzione:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                in_esecuzione = False
        
        schermo.fill(BIANCO)
        disegna_griglia(schermo, griglia, dimensione_cella)
        disegna_percorso(schermo, percorso, dimensione_cella)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
