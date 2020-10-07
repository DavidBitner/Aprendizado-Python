while True:
    matriz = []
    dados = []
    resposta = bResposta = 1
    n = int(input())
    if n == 0:
        break
    for linha in range(0, n):
        for coluna in range(0, n):
            dados.append(resposta)
            resposta *= 2
        matriz.append(dados[:])
        dados.clear()
        bResposta *= 2
        resposta = bResposta
    doidera = str(matriz[n - 1][n - 1])
    numero = len(doidera)
    for linha in range(0, len(matriz)):
        for coluna in range(0, len(matriz)):
            if coluna == 0:
                print(f"{matriz[linha][coluna]:{numero}}", end="")
            else:
                print(f" {matriz[linha][coluna]:{numero}}", end="")
        print()
    print()
