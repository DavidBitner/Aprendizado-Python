mil = mBarato = total = 0
barato = continuar = ' '


print('-' * 40)
print('BEM VINDO')
print('-' * 40)

while True:
    print('-' * 40)
    produto = str(input('Digite o nome do produto: ')).strip().capitalize()
    valor = float(input('Digite o valor do produto: R$'))
    print('-' * 40)

    total += valor

    if valor > 1000:
        mil += 1

    if mBarato == 0:
        mBarato = valor
        barato = produto
    elif valor < mBarato:
        mBarato = valor
        barato = produto

    while continuar not in 'SsNn':
        continuar = str(input('Deseja continuar? [S/N]: '))
        if continuar not in 'SsNn':
            print('Opção invalida, tente novamente!')
        else:
            break

    if continuar in 'Nn':
        print('\n\n')
        break

    continuar = ' '

print('-=' * 20)
print('COMPRA FINALIZADA')
print(f'R${total:.2f} TOTAL DA COMPRA')
print(f'{mil} produtos custam mais de R$1000,00')
print(f'{barato} é o nome do produto mais barato')
print('-=' * 20)
