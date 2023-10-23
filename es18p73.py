import math

list = [i**2 for i in range(0, 1000) if (i % 2 != 0) and (i**2 < 200)]

print(f"quadrati perfetti dispari: {list}")