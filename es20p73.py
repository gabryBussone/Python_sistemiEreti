max = 10

power = [[k * i for i in range (1, max + 1)] for k in range (1, max + 1)]

for k, tabellina in enumerate(power): 
    #tabellina è una lista 
    #power lista di liste 
    # enumerate: funzione che numera le liste e ritorna indicie e elemento
    print(f"Tabellina del {k + 1}: {tabellina}")

file = open("Data.txt", "w")

for k in range (max):
    file.write(f"{tabellina}\n")
    
file.close()   