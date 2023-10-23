import math

num = int(input("inserisci un numero: "))

esponente = int(math.log2(num))

lista = [2**i for i in range(0, esponente) if (2**i, )]

print(lista)