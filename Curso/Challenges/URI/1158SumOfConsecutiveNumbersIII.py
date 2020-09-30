n = int(input())
for i in range(0, n):
    resultado = 0
    A, B = input().split(" ")
    x, y = int(A), int(B)
    if x % 2 == 0:
        x += 1
    base = x + y * 2
    for impar in range(x, base, 2):
        resultado += impar
    print(resultado)
