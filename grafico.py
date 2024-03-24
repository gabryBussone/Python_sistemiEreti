import matplotlib.pyplot as plt
import csv

# Initialize lists to store data
mesi = []
mesi_n = []
temperature = []
giacca = []
scuola = []
videogame = []

csv_file_path = "./grafico.csv" 
with open(csv_file_path) as data_file:
    data_reader = csv.reader(data_file, delimiter=",")
    for row in data_reader:
        mesi.append(row[0])  # Month names
        mesi_n.append(int(row[1]))  # Month numbers
        temperature.append(float(row[2]))  # Temperature
        giacca.append(int(row[3]))  # Jacket
        scuola.append(int(row[4]))  # School
        videogame.append(int(row[5]))  # Videogame

# Plotting
fig, axs = plt.subplots(3, 1, figsize=(10, 8))
fig.suptitle("Analisi mensile")

axs[0].plot(mesi_n, temperature, "o-b", linewidth = 3)
axs[0].set_ylabel("Temperatura (°C)")
axs[0].grid()

axs[1].plot(mesi_n, giacca, "o-r", linewidth = 3)
axs[1].set_ylabel("Giorni con giacca")
axs[1].grid()

axs[2].plot(mesi_n, scuola, "o-g", label="Scuola", linewidth = 3)
axs[2].plot(mesi_n, videogame, "o-y", label="Videogame")
axs[2].set_ylabel("Attività giornaliere")
axs[2].legend()
axs[2].grid()

plt.xlabel("Mese")

plt.show()
