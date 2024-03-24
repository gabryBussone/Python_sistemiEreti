#NUMERI NARCISISTI

def eNarcisista(num):

    a = [int(x) for x in str(num)]
    somma_cubi = sum([x**3 for x in a])
    return somma_cubi == num

numeri_narcisisti = {}

for r in range(1, 999):

    if eNarcisista(r):
        numeri_narcisisti.append(r)

print("i numeri narcisisti sono: ")

for x in numeri_narcisisti:
    print(x)
