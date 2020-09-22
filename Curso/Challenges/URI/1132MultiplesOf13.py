x = int(input())
y = int(input())
maior = menor = soma = 0
if x > y:
    maior = x
    menor = y
else:
    maior = y
    menor = x
for i in range(menor, maior + 1):
    if i % 13 != 0:
        soma += i
print(soma)
