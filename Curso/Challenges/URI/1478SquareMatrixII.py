while True:
    dados = []
    matriz = []
    n = int(input())
    if n == 0:
        break
    for linha in range(0, n):
        for coluna in range(0, n):
            dados.append(0)
        matriz.append(dados[:])
        dados.clear()
    linha = 1
    adicao = 1
    bAdicao = 1
    doidera = 1
    while linha <= len(matriz):
        for linha in range(linha - 1, linha):
            for coluna in range(0, len(matriz)):
                if bAdicao == 1:
                    matriz[linha][coluna] += adicao
                    adicao += 1
                elif bAdicao > 1:
                    matriz[linha][coluna] += adicao
                    adicao -= 1
                    if adicao == 1:
                        bAdicao = 1
            bAdicao += doidera
            adicao = bAdicao
            linha += 1
            doidera += 1
        linha += 1

    for linha in range(0, len(matriz)):
        for coluna in range(0, len(matriz)):
            if coluna == 0:
                print(f"{matriz[linha][coluna]:3}", end="")
            else:
                print(f"{matriz[linha][coluna]:4}", end="")
        print()
    print()
