operacao = str(input())
soma = media = contador = 0
matriz = [[], [], [], [], [], [], [], [], [], [], [], []]
for linha in range(0, 12):
    for coluna in range(0, 12):
        n = float(input())
        matriz[linha].append(n)
for linha in range(0, 12):
    for coluna in range(0, 12):
        if coluna > 11 - linha:
            soma += matriz[coluna][linha]
            contador += 1
if operacao in "S":
    print(f"{soma:.1f}")
else:
    print(f"{soma / contador:.1f}")
