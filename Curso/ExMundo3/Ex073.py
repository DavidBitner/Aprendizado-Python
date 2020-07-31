campeonato = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico Paranaense', 'São Paulo', 'Internacional', 'Corinthians', 'Fortaleza', 'Goiás', 'Bahia', 'Vasco', 'Atlético Mineiro', 'Fluminense', 'Botafogo', 'Ceará', 'Cruzeiro', 'Csa', 'Chapecoense', 'Avaí')

posicaoChapecoense = campeonato.index('Chapecoense') + 1

print('\nEstes são todos os times do campeonato Brasileiro de futebol:')
print(campeonato)

print('\nOs ultimos 4 colocados da tabela são:')
print(campeonato[-4:])

print('\nA lista de times na ordem alfabética é:')
print(sorted(campeonato))

print(f'\nO time Chapecoense se encontra na {posicaoChapecoense}º posição')
