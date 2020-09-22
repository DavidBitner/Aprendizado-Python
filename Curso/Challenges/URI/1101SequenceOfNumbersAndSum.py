while True:
    A, B = input().split(" ")
    m, n = int(A), int(B)
    soma = maior = menor = 0
    if m <= 0 or n <= 0:
        break
    if m > n:
        maior = m
        menor = n
    else:
        maior = n
        menor = m
    for i in range(menor, maior + 1):
        soma += i
        print(f"{i} ", end="")
    print(f"Sum={soma}")
