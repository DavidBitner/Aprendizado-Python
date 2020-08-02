import random

'''
tupla = tuple

for c in range(0, 10):
    tupla[c] = random.randint(0, 11)
'''

'''maior = 0
menor = 0'''

'''a = random.randint(0, 10)
c = random.randint(0, 10)
d = random.randint(0, 10)
e = random.randint(0, 10)
b = random.randint(0, 10)'''

tupla = (random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10))

print('Os valores sorteados foram: ', end='')
for contador in range(0, len(tupla)):
    print(tupla[contador], end=' ')

print()

'''for contador in range(0, len(tupla)):
    if contador == 0:
        maior = tupla[contador]
        menor = tupla[contador]
    else:
        if tupla[contador] > maior:
            maior = tupla[contador]
        
        if tupla[contador] < menor:
            menor = tupla[contador]'''

print(f'O maior valor sorteado foi o {max(tupla)}')
print(f'O menor valor sorteado foi o {min(tupla)}')
