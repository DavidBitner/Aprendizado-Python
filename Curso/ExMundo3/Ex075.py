a = int(input('Digite um numero: '))
b = int(input('Digite outro numero:'))
c = int(input('Digite mais um numero: '))
d = int(input('Digite o ultimo numero: '))

tupla = (a, b, c, d)

pares = 0

for c in tupla:
    if c % 2 == 0:
        pares += 1

print(f'Você digitou os valores {tupla}')
print(f'O numero 9 aparece {tupla.count(9)} vezes')
print(f'O valor 3 apareceu na {tupla.index(3) + 1}º posição')
print(f'Os valores pares digitados foram {pares}')
