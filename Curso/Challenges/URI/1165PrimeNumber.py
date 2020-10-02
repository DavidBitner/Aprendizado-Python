n = int(input())
for i in range(0, n):
    divisores = 0
    p = int(input())
    for c in range(2, p):
        if p % c == 0:
            divisores += 1
            break
    if divisores == 0:
        print(f"{p} eh primo")
    else:
        print(f"{p} nao eh primo")
