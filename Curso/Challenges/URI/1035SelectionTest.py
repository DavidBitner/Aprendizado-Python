A, B, C, D = input().split(" ")
a, b, c, d = int(A), int(B), int(C), int(D)

if b > c and d > a and c + d > a + b and c > 0 and d > 0 and a % 2 == 0:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")
