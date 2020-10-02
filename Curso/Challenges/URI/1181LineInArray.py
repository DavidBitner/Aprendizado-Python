linha_escolhida = int(input())
operacao = str(input())
soma = media = 0
matriz = [[], [], [], [], [], [], [], [], [], [], [], []]
for linha in range(0, 12):
    for coluna in range(0, 12):
        n = float(input())
        matriz[linha].append(n)
for numero in matriz[linha_escolhida]:
    soma += numero
if operacao in "S":
    print(f"{soma:.1f}")
else:
    print(f"{soma / 12:.1f}")
