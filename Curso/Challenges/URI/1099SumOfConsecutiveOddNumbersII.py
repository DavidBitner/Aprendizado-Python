entrada = int(input())
soma = 0
for i in range(0, entrada):
    A, B = input().split(" ")
    x, y = int(A), int(B)
    if x >= y:
        inicio = y
        fim = x
    else:
        inicio = x
        fim = y
    for j in range(inicio + 1, fim):
        if j % 2 != 0:
            soma += j
    print(soma)
    soma = 0
