while True:
    try:
        dados = []
        matriz = []
        n = int(input())
        for linha in range(0, n):
            for coluna in range(0, n):
                dados.append(0)
            matriz.append(dados[:])
            dados.clear()
        # Numeros na diagonal
        for diagonal_principal in range(0, n):
            matriz[diagonal_principal][diagonal_principal] = 2
        for diagonal_secundaria in range(0, n):
            matriz[diagonal_secundaria][n - 1 - diagonal_secundaria] = 3

        # Matriz do numero 1
        for linha in range(n // 3, n - n // 3):
            for coluna in range(n // 3, n - n // 3):
                matriz[linha][coluna] = 1

        # Matriz do numero 4
        matriz[n // 2][n // 2] = 4

        # Print da Matriz completa
        for linha in range(0, len(matriz)):
            for coluna in range(0, len(matriz)):
                if coluna == 0:
                    print(f"{matriz[linha][coluna]}", end="")
                else:
                    print(f"{matriz[linha][coluna]}", end="")
            print()
        print()
    except EOFError:
        break
