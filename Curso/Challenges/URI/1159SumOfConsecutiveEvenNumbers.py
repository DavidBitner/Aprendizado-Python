while True:
    resultado = 0
    x = int(input())
    if x == 0:
        break
    if x % 2 != 0:
        x += 1
    for i in range(x, x + 10, 2):
        resultado += i
    print(resultado)
