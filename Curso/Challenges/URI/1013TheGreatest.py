A, B, C = input().split(" ")
a, b, c = int(A), int(B), int(C)
maior = a
if b > maior:
    maior = b
if c > maior:
    maior = c
print("{} eh o maior".format(maior))
