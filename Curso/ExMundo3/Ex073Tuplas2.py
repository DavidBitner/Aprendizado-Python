campeonato = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico Paranaense', 'São Paulo', 'Internacional', 'Corinthians', 'Fortaleza', 'Goiás', 'Bahia', 'Vasco', 'Atlético Mineiro', 'Fluminense', 'Botafogo', 'Ceará', 'Cruzeiro', 'Csa', 'Chapecoense', 'Avaí')

posicaoChapecoense = campeonato.index('Chapecoense') + 1

print('\nEstes são todos os times do campeonato Brasileiro de futebol:')
print(campeonato)

print('\nEstes são os 5 primeiros times na tabela:')
print(campeonato[0:5])

print('\nOs ultimos 4 colocados da tabela são:')
print(campeonato[-4:])

print('\nA lista de times na ordem alfabética é:')
print(sorted(campeonato))

print(f'\nO time Chapecoense se encontra na {posicaoChapecoense}º posição')

print(f'\nO time São Paulo se encontra na {campeonato.index("São Paulo") + 1}º posição')
