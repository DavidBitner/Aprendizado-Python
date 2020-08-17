tupla = (int(input('Digite um numero: ')),
         int(input('Digite outro numero: ')),
         int(input('Digite mais um numero: ')),
         int(input('Digite o ultimo numero: ')))
pares = 0
for c in tupla:
    if c % 2 == 0:
        pares += 1
print(f'\nVocê digitou os valores {tupla}')
print(f'O numero 9 aparece {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O valor 3 apareceu na {tupla.index(3) + 1}º posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')

print(f'Os valores pares digitados foram {pares}')
