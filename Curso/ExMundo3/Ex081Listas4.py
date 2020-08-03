lista = []

while True:
    n = int(input('Digite um numero: '))

    lista.append(n)

    while True:
        continuar = str(input('Quer continuar? [S/N] ')).strip()

        if continuar in 'SsNn':
            break

    if continuar in 'Nn':
        break

lista.sort(reverse=True)
print(f'Você digitou {len(lista)} elementos')
print(f'Os valores em ordem decrescente são {lista}')

if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista')
