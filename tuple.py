#tuple

t = (3, 4, 10, 2)
t[1] = 9
print(t[0])

punto = (3, 4)
x, y = punto #assegnazione multipla
print(x)


#lambda function: utile per definire funzioni brevi

def somma(a, b):
    return a + b

somma = lambda x, y: x + y

x, y = 10, 4
print(somma(x, y))

lista = [10, 4]
print(somma(*lista)) #operatore di spacchettamento della lista sui parametri