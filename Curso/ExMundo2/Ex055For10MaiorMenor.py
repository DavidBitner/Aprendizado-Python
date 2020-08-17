maior = 0
menor = 0
for c in range(0, 5):
    peso = float(input('Digite o peso da {}º pessoa: '.format(c + 1)))
    if c == 0:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso foi {:.1f} e o menor peso foi {:.1f}'.format(maior, menor))
