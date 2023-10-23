def main():

    x = [0, 1, 2, 3, 5, 6, 7, 8]
    lung = len(x)
    mezzo = lung // 2  # // divisione intera( mi da un numero intero della divisione)

    lista1 = x[:mezzo] #va fdall'inizio fino a meta della lista
    lista2 = x[mezzo:] #va da metà alla fine della lista

    print(f"La lista 1 è: {lista1}, La lista 2 è: {lista2}")

    lista1.append(lista2[0])

    print(f"La lista 1 con il 5 è: {lista1}")

if __name__ == "__main__":
    main()
