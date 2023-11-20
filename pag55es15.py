def main():
    nome = str(input("inserire un nome: "))
    nome_ = nome[0] + "*" * (len(nome) - 1)
    print("nome con solo il primo carattere: ", nome_)

if __name__ == "__main__":
    main()