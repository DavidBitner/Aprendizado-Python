lista = []

while True:
    n = int(input('Digite um valor: '))

    if n in lista:
        print('Valor duplicado! Não vou adicionar...')
    else:
        lista.append(n)
        print('Valor adicionado com sucesso...')

    while True:
        continuar = str(input('Quer continuar? [S/N] ')).strip()

        if continuar in 'SsNn':
            break

    if continuar in 'Nn':
        break

lista.sort()
print('-=' * 40)
print(f'Você digitou os valores {lista}')
