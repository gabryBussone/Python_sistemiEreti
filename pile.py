def push(pila, elemento):
    pila.append(elemento)

def pop (pila):
    x = pila.pop()
    return x

def main():

    parentesi_aperte = ["{", "[", "("]
    stringa = "{1+[2+3]*5"
    pila = []
    for carattere in stringa:
        if carattere in parentesi_aperte:
            push(pila, carattere)
    print(pila)

if __name__ == "__main__":
    main()