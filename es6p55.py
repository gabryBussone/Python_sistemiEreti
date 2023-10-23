def main():
    
    parola = "elefante"
    n = len(parola) #conta quanti caratteri ha la parola elefante
    for i in range(n):
        if i % 2 != 0:
            print(parola[i])

def main():
    
    parola = "elefante"
    print(parola[1::2]) # stampo caratteri dispari

if __name__ == "__main__":
    main()
