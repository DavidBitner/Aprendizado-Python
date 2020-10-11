entrada = int(input())
pessoas = input().split(" ")
menor = 0
escolhida = 0
for i in range(0, len(pessoas)):
    base = int(pessoas[i])
    if i == 0:
        escolhida = i
        menor = base
    elif base < menor:
        escolhida = i
        menor = base
print(escolhida + 1)
