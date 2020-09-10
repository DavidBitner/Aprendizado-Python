lista = []
pares = 0
for i in range(0, 5):
    lista.append(float(input()))
    if lista[i] % 2 == 0:
        pares += 1
print(f"{pares} valores pares")
