def completa8bit(strbin):
    b = strbin[2:]
    l = len(b)
    return "0"*(8 - l) + b



def main():

    adress = "192.168.0.1"

    groups = adress.split(".") # separa una stringa in stringhe dove c'è il punto

    print(groups) #stampo la stringa di stringhe

    groups = [int (group) for group in groups]  #trasformo le stringhe in interi

    print(groups)

    groups_bin = [bin(group) for group in groups]  #trasformo in numeir binari

    print(groups_bin)

    print(completa8bit(groups_bin[0]))   #tolgo lo 0b davanti e aggiungo gli 0 necessari

    groups_strbin = [completa8bit(strbin) for strbin in groups_bin]

    print(groups_strbin)

    print(".".join(groups_strbin)) #mette il punto tra le stringhe

    
if __name__ == "__main__":
    main()
