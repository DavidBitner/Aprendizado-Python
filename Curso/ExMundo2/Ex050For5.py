s = 0
e = 6
p = 1
r = int(0)

for c in range(s, e, p):
    n = int(input('Digite um numero: '))

    if n % 2 == 0:
        r += n

print(r)
