#scrivi un programma in python che chieda un numero all'utente e gli comunichi se questo numero è divisibile per 3 oppure no. Per verificare se la divisibilità può esserti utile l'operatore resto %. l'espressione a%b calcola il resto della divisione

def main(): 
    
    n = float(input("inserisci un numero: "))
    
    if n % 3 == 0:
        print(f"Il numero {n} è divisibile per 3")
    else:
        print(f"Il numero {n} non è divisibile per 3")

if __name__ == "__main__":
    main()