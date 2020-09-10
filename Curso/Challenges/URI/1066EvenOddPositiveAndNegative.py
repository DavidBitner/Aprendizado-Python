lista = []
pares = impares = positivos = negativos = 0
for i in range(0, 5):
    lista.append(float(input()))
    if lista[i] % 2 == 0:
        pares += 1
    else:
        impares += 1
    if lista[i] > 0:
        positivos += 1
    elif lista[i] < 0:
        negativos += 1
print(f"{pares} valor(es) par(es)")
print(f"{impares} valor(es) impar(es)")
print(f"{positivos} valor(es) positivo(s)")
print(f"{negativos} valor(es) negativo(s)")
