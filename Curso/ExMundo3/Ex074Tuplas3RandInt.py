import random

tupla = (random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10))
print('Os valores sorteados foram: ', end='')
for contador in range(0, len(tupla)):
    print(tupla[contador], end=' ')
print()
print(f'O maior valor sorteado foi o {max(tupla)}')
print(f'O menor valor sorteado foi o {min(tupla)}')
