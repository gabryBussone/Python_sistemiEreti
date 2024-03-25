import csv
import matplotlib.pyplot as plt


years = []
cumulative_mass_variation = []

# lettura dei dati dal file CSV
with open('datiGhiacciai.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        year = int(row[0])
        mass_variation = int(row[3])  # considero solo la variazione cumulativa della massa
        years.append(year)
        cumulative_mass_variation.append(mass_variation)

# creazione del grafico
plt.figure(figsize=(10, 6))
plt.plot(years, cumulative_mass_variation, marker='o', color='b', linestyle='-')
plt.title('Variazione Cumulativa della Massa dell\'Aria nel Tempo')
plt.xlabel('Anno')
plt.ylabel('Variazione Cumulativa della Massa [m w.e. o 1000 kg m^-2]')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

# mostra il grafico
plt.show()
