entrada = int(input())
for i in range(0, entrada):
    A, B, C = input().split(" ")
    a, b, c = float(A), float(B), float(C)
    media = (a * 2 + b * 3 + c * 5) / (2 + 3 + 5)
    print(f"{media:.1f}")
