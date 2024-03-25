import csv
import matplotlib.pyplot as plt

anni = []
temperature = []

# leggi i dati dal file CSV
with open('datiTemp.csv', newline='') as csvfile:
    lettore = csv.reader(csvfile, delimiter=' ')
    for riga in lettore:
        anno, temperatura = riga[0].split(',')
        anni.append(int(anno))
        temperature.append(float(temperatura))

# crea il grafico
plt.figure(figsize=(10, 6))
plt.plot(anni, temperature, marker='o', color='b', linestyle='-')
plt.title('Temperature medie annuali')
plt.xlabel('Anno')
plt.ylabel('Temperatura (°C)')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

# mostra il grafico
plt.show()
