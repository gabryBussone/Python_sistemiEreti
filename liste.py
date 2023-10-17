def print_list(l):                    #cambia sostanzialmente il tipo di stampa, provare sul terminale
    print("\nla lista è: ", end=" ")
    for elemento in l:
        print(elemento, end=" ")
    print("\n")


def main():
    #liste

    l = [1,2,3,4,"c",14.5]
    r = [10, 20, 30]
    #print_list(l + r) #concatenazione tra due liste
    #print_list(3 * r) #comcatenazione multipla

    #vogliamo permettere all'utente di caricare una lista

    lista = []
    num = 1
    while num > 0:
        num = input("scrivi un numero: (-1 per interompere): ")
        if num > 0:
            lista.append(num) #aggiunge num alla lista
            
    print_list(lista)
    


if __name__=="__main__":
    main()