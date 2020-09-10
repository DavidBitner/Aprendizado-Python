a = int(input())
b = int(input())
soma = 0
if a > b:
    inicio = b
    fim = a
else:
    inicio = a
    fim = b
for i in range(inicio + 1, fim):
    if i % 2 != 0:
        soma += i
print(soma)
