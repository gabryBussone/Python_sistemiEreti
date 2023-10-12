# SCLICING DI STRINGHE
s = "ciao come stai?"
print(f"il primo carattere è {s[0]}")
print(f"l'ultimo carattere è {s[-1]}")
print(f"il penultimo carattere carattere è {s[-2]}")
print(f"l'ultimo carattere carattere è {s[len(s) -1]}") #C -style DA NON USARE

print(s[3:7]) # dal carattere 3 al carattere 7 escluso
print(f"tutta la stringa esclusi il 1° e l'ultimo carattere: {s[1:-1]}")
print(f"tutta la stringa escluso il 1° carattere: {s[1:]}")
print(f"tutta la stringa escluso l'ultimo carattere: {s[:-1]}")
