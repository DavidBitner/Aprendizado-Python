from random import randint
from time import sleep
jogadores = []
jogada = {}

for c in range(0, 4):
    jogada['jogador'] = c + 1
    jogada['jogada'] = randint(1, 6)
    jogadores.append(jogada.copy())
    jogada.clear()

print('Valores sorteados:')
for c in range(0, 4):
    print(f'    O jogador{jogadores[c]["jogador"]} tirou {jogadores[c]["jogada"]}')

jogadores.sort()

print('Ranking dos jogadores:')
for c in range(0, 4):
    print(f'    {c}º lugar: {jogadores[c]["jogador"]} com {jogadores[c]["jogada"]}')


INCOMPLETO