A, B, C = input().split(" ")
a, b, c = float(A), float(B), float(C)
if b - c < a < b + c and a - c < b < a + c and a - b < c < a + b:
    perimetro = a + b + c
    print(f"Perimetro = {perimetro:.1f}")
else:
    area = ((a + b) * c) / 2
    print(f"Area = {area:.1f}")
