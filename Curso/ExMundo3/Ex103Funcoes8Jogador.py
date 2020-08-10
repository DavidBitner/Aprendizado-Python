def ficha(jogador, gols):
    if jogador == '':
        jogador = '<jogador desconhecido>'
    if gols == '':
        gols = 0
    print(f'O jogador {jogador} fez {gols} gol(s) no campeonato')


# Programa Principal
print('-' * 30)
j = str(input('Nome do Jogador: '))
g = int(input('Numero de gols: ') or '0')
ficha(j, g)
