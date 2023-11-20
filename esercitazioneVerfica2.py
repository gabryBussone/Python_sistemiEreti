def main():
    with open("covid-19_gen1.txt", "r") as file:
        sequenza_genomica = file.read().replace('\n', '')

    occorrenze_A = sequenza_genomica.count('A')
    occorrenze_T = sequenza_genomica.count('T')
    occorrenze_G = sequenza_genomica.count('G')
    occorrenze_C = sequenza_genomica.count('C')

    print(f"Occorrenze di A: {occorrenze_A}")
    print(f"Occorrenze di T: {occorrenze_T}")
    print(f"Occorrenze di G: {occorrenze_G}")
    print(f"Occorrenze di C: {occorrenze_C}")

    sequenza_spike = "ATGTTTGTTTTT"
    posizione_spike = sequenza_genomica.find(sequenza_spike)

    print(f"La sequenza spike è presente alla posizione: {posizione_spike}")


if __name__ == "__main__":
    main()


