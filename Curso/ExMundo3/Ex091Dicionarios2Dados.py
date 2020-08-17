from random import randint
from time import sleep
from operator import itemgetter

jogada = {'jogador1': randint(1, 6),
          'jogador2': randint(1, 6),
          'jogador3': randint(1, 6),
          'jogador4': randint(1, 6)}
ranking = {}
print('Valores sorteados:')
for k, v in jogada.items():
    print(f'{k} tirou {v} no dado.')
    sleep(0.3)
ranking = sorted(jogada.items(), key=itemgetter(1), reverse=True)
print('-' * 50)
print('== RANKING DOS JOGADORES ==')
for c1, c2 in enumerate(ranking):
    print(f'{c1 + 1}º lugar: {c2[0]} com {c2[1]}.')
    sleep(0.3)
