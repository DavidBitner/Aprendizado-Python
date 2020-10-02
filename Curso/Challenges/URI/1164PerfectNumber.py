n = int(input())
for i in range(0, n):
    p = int(input())
    soma = 0
    for c in range(1, p):
        if p % c == 0:
            soma += c
    if soma == p:
        print(f"{p} eh perfeito")
    else:
        print(f"{p} nao eh perfeito")
