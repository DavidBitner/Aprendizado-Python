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
    resultado = 1
    cima = 0
    esquerda = 0
    baixo = n - 1
    direita = n - 1
    if n % 2 == 0:
        meio = n / 2
    else:
        meio = (n + 1) / 2
    while resultado <= meio:
        temp = esquerda
        while temp <= direita:
            matriz[cima][temp] = resultado
            matriz[baixo][temp] = resultado
            temp += 1
        temp = (cima + 1)
        while temp < baixo:
            matriz[temp][esquerda] = resultado
            matriz[temp][direita] = resultado
            temp += 1
        resultado += 1
        cima += 1
        baixo -= 1
        esquerda += 1
        direita -= 1
    for linha in range(0, len(matriz)):
        for coluna in range(0, len(matriz)):
            if coluna == 0:
                print(f"  {matriz[linha][coluna]}", end="")
            else:
                print(f"{matriz[linha][coluna]:4d}", end="")
        print()
    print()
