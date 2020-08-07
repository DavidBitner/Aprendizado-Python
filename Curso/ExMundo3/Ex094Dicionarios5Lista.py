pessoas = list()
pessoa = dict()
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

for c in pessoas:
    if c['sexo'] in 'Ff':
        print(c['nome'], end=' ')
print(f'\nLista das pessoas que estão acima da média:\n')

for c in pessoas:
    if c['idade'] > media:
        for k, v in c.items():
            print(f'{k} = {v}', end='; ')
