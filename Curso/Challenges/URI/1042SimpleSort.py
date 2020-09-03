A, B, C = input().split(" ")
a, b, c = int(A), int(B), int(C)
maior = meio = menor = 0
if a < b and a < c:
    menor = a
    if b < c:
        meio = b
        maior = c
    if c < b:
        meio = c
        maior = b
if b < c and b < a:
    menor = b
    if a < c:
        meio = a
        maior = c
    if c < a:
        meio = c
        maior = a
if c < b and c < a:
    menor = c
    if b < a:
        meio = b
        maior = a
    if a < b:
        meio = a
        maior = b
print(menor)
print(meio)
print(maior)
print()
print(a)
print(b)
print(c)
