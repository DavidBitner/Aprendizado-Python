from math import sqrt

A, B, C = input().split(" ")
a, b, c = float(A), float(B), float(C)
triangulo = b * b - 4 * a * c
try:
    r1 = (-b + sqrt(triangulo)) / (a * 2)
    r2 = (-b - sqrt(triangulo)) / (a * 2)
    print(f"R1 = {r1:.5f}")
    print(f"R2 = {r2:.5f}")
except ValueError:
    print("Impossivel calcular")
except ZeroDivisionError:
    print("Impossivel calcular")
