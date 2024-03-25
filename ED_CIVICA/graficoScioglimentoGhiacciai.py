import csv
import matplotlib.pyplot as plt

anni = []
variazione_massa_cumulativa = []

# Lettura dei dati dal file CSV
with open('datiGhiacciai.csv', newline='') as csvfile:
    lettore = csv.reader(csvfile)
    for riga in lettore:
        anno = int(riga[0])
        variazione_massa = int(riga[3])  # Considero solo la variazione cumulativa della massa
        anni.append(anno)
        variazione_massa_cumulativa.append(variazione_massa)

# Creazione del grafico
plt.figure(figsize=(10, 6))
plt.plot(anni, variazione_massa_cumulativa, marker='o', color='b', linestyle='-')
plt.title('Variazione Cumulativa della Massa dell\'Aria nel Tempo')
plt.xlabel('Anno')
plt.ylabel('Variazione Cumulativa della Massa [m w.e. o 1000 kg m^-2]')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

# Mostra il grafico
plt.show()
