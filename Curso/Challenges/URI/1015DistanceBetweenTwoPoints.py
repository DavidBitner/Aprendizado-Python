from math import sqrt

A, B = input().split(" ")
C, D = input().split(" ")
x1, y1 = float(A), float(B)
x2, y2 = float(C), float(D)
base1 = (x2 - x1) * (x2 - x1)
base2 = (y2 - y1) * (y2 - y1)
distance = sqrt(base1 + base2)
print("{:.4f}".format(distance))
