from random import randint
from time import sleep

print('-' * 42)
print(f'{"JOGA NA MEGA SENA":^42}')
print('-' * 42)
jogos = []
jogo = []
numero = 0
cont2 = 0

n = int(input('Quantos jogos você quer que eu sorteie? '))

for cont1 in range(0, n):
    while cont2 < 6:
        numero = randint(1, 60)
        if numero not in jogo:
            jogo.append(numero)
            cont2 += 1
    jogo.sort()
    jogos.append(jogo[:])
    jogo.clear()
    cont2 = 0

print('-=' * 5, end='')
print(f'  Sorteando {n} jogos  ', end='')
print('-=' * 5)

for c in range(0, len(jogos)):
    print(f'Jogo {c + 1}: {jogos[c]}')
    sleep(0.5)
