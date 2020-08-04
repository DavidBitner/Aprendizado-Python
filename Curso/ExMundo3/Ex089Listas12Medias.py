lista = list()
dados = list()

while True:
    dados.append(str(input('Digite o nome: ').strip().capitalize()))
    dados.append(float(input('Nota 1: ')))
    dados.append(float(input('Nota 2: ')))
    lista.append(dados[:])
    dados.clear()

    while True:
        continuar = str(input('Quer continuar? [S/N] ')).strip()

        if continuar in 'SsNn':
            break

    if continuar in 'Nn':
        break

for c in range(0, len(lista)):
    lista[c].append((lista[c][1] + lista[c][2]) / 2)

print('-=' * 40)
print(f'{"No.":<4}', end='')
print(f'{"NOME":<20}', end='')
print(f'{"MÉDIA":<5}')
print('-' * 34)

for cont1 in range(0, len(lista)):
    print(f'{cont1:<4}', end='')
    print(f'{lista[cont1][0]:<20}', end='')
    print(f'{lista[cont1][3]:>5.1f}')

while True:
    print('-' * 40)
    escolha = int(input('Mostrar notas de qual aluno? (999 interrompe) '))
    if escolha == 999:
        break
    elif escolha >= len(lista):
        print('Opção invalida')
    else:
        print(f'Notas de {lista[escolha][0]} são {lista[escolha][1:3]}')
print('-' * 40)
