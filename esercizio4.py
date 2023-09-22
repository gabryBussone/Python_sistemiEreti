#un programma che chieda 2 numeri float all'utente e stampi una stringa con dentro i due numeri in nome decrescente

n1 = float(input("inserisci il primo numero: "))
n2 = float(input("inserisci il secondo numero: "))

if (n1 < n2):
    n1, n2 = n2, n1
else:
    print(f"ordine decrescente: {n1} {n2}")
    
