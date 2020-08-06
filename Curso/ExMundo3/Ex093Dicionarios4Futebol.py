jogador = dict()
gols = list()

jogador['nome'] = str(input('Nome do Jogador: ')).strip().capitalize()
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, partidas):
    gols.append(int(input(f'Quantos gols na partida {c + 1}? ')))
jogador['gols'] = gols.copy()
jogador['total'] = 0
for c in gols:
    jogador['total'] += c

print('_' * 50)
print(jogador)
print('_' * 50)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')

print('_' * 50)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for c in range(0, len(jogador['gols'])):
    print(f'    => Na partida {c + 1}, fez {jogador["gols"][c]} gols.')
print(f'Foi um total de {jogador["total"]} gols')
