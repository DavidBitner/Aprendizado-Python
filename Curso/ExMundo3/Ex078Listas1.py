lista = []
posicaoMenor = []
posicaoMaior = []
maior = 0
menor = 0

for c in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {c}: ')))

print(f'Você digitou os valores: {lista}')

'''print(f'O maior valor está na posição {lista.index(max(lista)) + 1} e foi o {max(lista)}')

print(f'O menor valor está na posição {lista.index(min(lista)) + 1} e foi o {min(lista)}')
'''

for c, valor in enumerate(lista):
    if maior == 0:
        maior = valor
        posicaoMaior.append(c)
    elif valor > maior:
        maior = valor
        posicaoMaior.clear()
        posicaoMaior.append(c)
    elif valor == maior:
        posicaoMaior.append(c)
    
    if menor == 0:
        menor = valor
        posicaoMenor.append(c)
    elif valor < menor:
        menor = valor
        posicaoMenor.clear()
        posicaoMenor.append(c)
    elif valor == menor:
        posicaoMenor.append(c)
    
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
