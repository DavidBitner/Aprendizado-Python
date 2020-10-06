while True:
    try:
        dados = []
        matriz = []
        n = int(input())
        for linha in range(0, n):
            for coluna in range(0, n):
                dados.append(3)
            matriz.append(dados[:])
            dados.clear()
        base = n - 1
        for i in range(0, n):
            matriz[i][i] = 1
            matriz[i][base] = 2
            base -= 1
        for linha in range(0, len(matriz)):
            for coluna in range(0, len(matriz)):
                if coluna == 0:
                    print(f"{matriz[linha][coluna]}", end="")
                else:
                    print(f"{matriz[linha][coluna]}", end="")
            print()
    except EOFError:
        break
