def ficha(jogador, gols):
    if jogador == '':
        jogador = '<jogador desconhecido>'
    if not gols.isnumeric():
        gols = 0
    print(f'O jogador {jogador} fez {gols} gol(s) no campeonato')


# Programa Principal
print('-' * 30)
j = str(input('Nome do Jogador: '))
g = str(input('Numero de gols: '))
ficha(j, g)
