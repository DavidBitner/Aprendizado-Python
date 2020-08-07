jogadores = list()
jogador = dict()
gols = list()
contador = 0

while True:
    jogador['nome'] = str(input('Nome do Jogador: ')).strip().capitalize()
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(0, partidas):
        gols.append(int(input(f'Quantos gols na partida {c + 1}? ')))
    jogador['gols'] = gols.copy()
    jogador['total'] = 0
    for c in gols:
        jogador['total'] += c

    jogadores.append(jogador.copy())
    jogador.clear()
    gols.clear()

    while True:
        continuar = str(input('Quer continuar? [S/N] ')).strip()

        if continuar in 'SsNn':
            break

    if continuar in 'Nn':
        break

print('_' * 70)

print(f'{"cod":<3} {"nome":<15} {"gols":<20} {"total":<5}')
for c in range(0, len(jogadores)):
    print(f'{c:>3} {jogadores[c]["nome"]:<15} {str(jogadores[c]["gols"]):<20} {jogadores[c]["total"]:<5}')

print('_' * 70)

while True:
    escolha = int(input('Mostrar dados de qual jogador? [999 sair] '))
    if escolha == 999:
        break
    elif escolha < len(jogadores):
        print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[escolha]["nome"]}')
        for c1 in range(0, len(jogadores[escolha]['gols'])):
            print(f'No jogo {c1 + 1} fez ', end='')
            print(jogadores[escolha]['gols'][contador])
            contador += 1
        contador = 0
    else:
        print(f'ERRO! Não existe jogador com código {escolha}! Tente novamente')
    print('_' * 70)
