def main(): 
    file = open("rubrica.txt", "r")
    righe = file.readlines()
    file.close

    rubrica = {}

    print(righe)
    for riga in righe:
        campi = riga.split(", ")
        numeroTelefonico = int(campi[1].replace("\n", ""))
        nome = campi[0]
        rubrica[numeroTelefonico] = nome
    
    print(rubrica)

if __name__ == "__main__":
    main()



