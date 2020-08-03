lista = []
posicaoMenor = []
posicaoMaior = []
maior = 0
menor = 0

for c in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {c}: ')))

    if c == 0:
        maior = menor = lista[c]
        posicaoMenor.append(c)
        posicaoMaior.append(c)
    else:
        if lista[c] > maior:
            maior = lista[c]
            posicaoMaior.clear()
            posicaoMaior.append(c)
        elif lista[c] == maior:
            posicaoMaior.append(c)

        if lista[c] < menor:
            menor = lista[c]
            posicaoMenor.clear()
            posicaoMenor.append(c)
        elif lista[c] == menor:
            posicaoMenor.append(c)

print(f'Você digitou os valores: {lista}')

if len(posicaoMaior) > 1:
    print(f'O maior valor digitado foi o {maior} e ele se encontra nas posições ', end='')
    for valores in posicaoMaior:
        print(valores, end=' ')
    print()
else:
    print(f'O maior valor digitado foi o {maior} e ele se encontra na posição {posicaoMaior[0]}')

if len(posicaoMenor) > 1:
    print(f'O menor valor digitado foi o {menor} e ele se encontra nas posições ', end='')
    for valores in posicaoMenor:
        print(valores, end=' ')
else:
    print(f'O menor valor digitado foi o {menor} e ele se encontra na posição {posicaoMenor[0]}')
