resposta = 's'
media = basemedia = maior = 0
menor = -1

while resposta in 's':
    n = int(input('Digite um numero: '))
    media += n
    basemedia += 1

    if n > maior:
        maior = n

    if menor == -1:
        menor = n
    elif n < menor:
        menor = n

    resposta = str(input('Deseja continuar digitando? [S/N]: ')).strip().lower()

    while resposta != 's' and resposta != 'n':
        resposta = str(input('Opção invalida, digite "S" para continuar digitando ou "N" para parar: '))

media /= basemedia

print('A média dos valores digitados é {:.1f}'.format(media))
print('O maior valor é o {}'.format(maior))
print('O menor valor é o {}'.format(menor))
