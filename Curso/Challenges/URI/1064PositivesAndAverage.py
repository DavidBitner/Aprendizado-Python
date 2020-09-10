lista = []
positivos = media = divisao = 0
for i in range(0, 6):
    lista.append(float(input()))
    if lista[i] > 0:
        positivos += 1
        media += lista[i]
        divisao += 1
media /= divisao
print(f"{positivos} valores positivos")
print(f"{media:.1f}")
