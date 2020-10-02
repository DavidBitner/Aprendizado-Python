n = int(input())
X = input().split()
x = []
menor = posicao = 0
for thing in X:
    if "\t" in thing:
        thing.replace("\t", "")
    x.append(int(thing))
for i in range(0, len(x)):
    if menor == 0 and posicao == 0:
        menor = x[i]
    elif x[i] < menor:
        menor = x[i]
        posicao = i
print(f"Menor valor: {menor}")
print(f"Posicao: {posicao}")
