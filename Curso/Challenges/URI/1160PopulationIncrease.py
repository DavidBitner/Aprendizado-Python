n = int(input())
for i in range(0, n):
    A, B, C, D = input().split(" ")
    cidade_a, cidade_b, crescimento_a, crescimento_b = int(A), int(B), float(C), float(D)
    resultado = 0
    while cidade_a <= cidade_b:
        resultado += 1
        if resultado == 101:
            break
        cidade_a = (cidade_a + (cidade_a * crescimento_a / 100)) // 1
        cidade_b = (cidade_b + (cidade_b * crescimento_b / 100)) // 1
    if resultado <= 100:
        print(f"{resultado} anos.")
    else:
        print(f"Mais de 1 seculo.")
