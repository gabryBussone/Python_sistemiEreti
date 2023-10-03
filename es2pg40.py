def main(): 
    
    n = float(input("inserisci un numero: "))
    
    if n % 2 == 0:
        print(f"Il numero {n} è divisibile per 2")
    else:
        print(f"Il numero {n} non è divisibile per 2")
    
    if n % 3 == 0:
        print(f"Il numero {n} è divisibile per 3")
    else:
        print(f"Il numero {n} non è divisibile per 3")
    
    if n % 5 == 0:
        print(f"Il numero {n} è divisibile per 5")
    else:
        print(f"Il numero {n} non è divisibile per 5")


if __name__ == "__main__":
    main()