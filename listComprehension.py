# list comprehension
# lista con i primi 5 quadrati perfetti
import random
quadrati = [i*i for i in range(1,6)] #6 escluso 
numeri_interi = [i for i in range (1,11)]
stringhe = ["computer", "cellulare", "laptop"]
stringhe_c = [parola for parola in stringhe if parola[0] == "c"]
voti = [random.randint(2, 10) for i in range(0, 10)]
voti_insuff = [voto for voto in voti if voto < 6]
print(voti)
print(voti_insuff)
print(stringhe_c)
print(quadrati)
print(numeri_interi)