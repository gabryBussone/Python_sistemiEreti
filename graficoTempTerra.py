import csv
import matplotlib.pyplot as plt

# Inizializza le liste per memorizzare i dati
anni = []
temperature = []

# Leggi i dati dal file CSV
with open('datiTemp.csv', newline='') as csvfile:
    lettore = csv.reader(csvfile, delimiter=' ')
    for riga in lettore:
        anno, temperatura = riga[0].split(',')
        anni.append(int(anno))
        temperature.append(float(temperatura))

# Crea il grafico
plt.figure(figsize=(10, 6))
plt.plot(anni, temperature, marker='o', color='b', linestyle='-')
plt.title('Temperature medie annuali')
plt.xlabel('Anno')
plt.ylabel('Temperatura (°C)')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

# Mostra il grafico
plt.show()
