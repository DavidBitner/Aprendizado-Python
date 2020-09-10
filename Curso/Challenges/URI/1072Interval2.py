entrada = int(input())
lista = []
dentro = fora = 0
for i in range(0, entrada):
    lista.append(int(input()))
    if 10 <= lista[i] <= 20:
        dentro += 1
    else:
        fora += 1
print(f"{dentro} in")
print(f"{fora} out")
