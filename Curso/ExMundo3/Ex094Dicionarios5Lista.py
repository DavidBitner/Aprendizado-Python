pessoas = list()
pessoa = dict()
mulheres = list()
contador = 0
media = 0

while True:
    pessoa['nome'] = str(input('Nome: ')).strip().capitalize()

    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F/O] '))
        if pessoa['sexo'] in 'FfMmOo':
            break

    pessoa['idade'] = int(input('Idade: '))
    media += pessoa['idade']

    if pessoa['sexo'] in 'Ff':
        mulheres.append(pessoa['nome'])

    pessoas.append(pessoa.copy())

    pessoa.clear()
    contador += 1

    while True:
        continuar = str(input('Quer continuar? [S/N] ')).strip()

        if continuar in 'SsNn':
            break

    if continuar in 'Nn':
        break

media /= contador

print('-' * 50)
print(f'O grupo tem {len(pessoas)} pessoas.')
print(f'A média de idade é de {media:.2f}')
print(f'As mulheres cadastradas foram: ', end='')

for c in mulheres:
    print(c, end=' ')
print(f'\nLista das pessoas que estão acima da média:\n')

for c1 in range(0, len(pessoas)):
    if pessoas[c1]['idade'] > media:
        for k, v in pessoas[c1].items():
            print(f'{k} = {v}', end='; ')
        print('\n')

'''
for k, v in dicionario.items():
    print(f'O {k} é {v}')
= O nome é Pedro
O idade é 25
O sexo é m'''