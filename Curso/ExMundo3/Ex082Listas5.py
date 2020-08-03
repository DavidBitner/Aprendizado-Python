lista = []
pares = []
impares = []

while True:
    n = int(input('Digite um numero: '))

    lista.append(n)

    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

    while True:
        continuar = str(input('Quer continuar? [S/N] ')).strip()

        if continuar in 'SsNn':
            break

    if continuar in 'Nn':
        break

print('-=' * 40)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')
