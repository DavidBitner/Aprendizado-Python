entrada = int(input())
for i in range(0, entrada):
    A, B = input().split(" ")
    x, y = int(A), int(B)
    if y == 0:
        print("divisao impossivel")
    else:
        resultado = x / y
        print(f"{resultado:.1f}")
