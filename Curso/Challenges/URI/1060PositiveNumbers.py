lista = []
positivos = 0
for i in range(0, 6):
    lista.append(float(input()))
    if lista[i] > 0:
        positivos += 1
print(f"{positivos} valores positivos")
