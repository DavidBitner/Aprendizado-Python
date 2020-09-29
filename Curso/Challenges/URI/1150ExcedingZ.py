x = int(input())
z = int(input())
while z <= x:
    z = int(input())
soma = x
contador = 1
base = x + 1
while soma <= z:
    soma += base
    base += 1
    contador += 1
print(contador)
