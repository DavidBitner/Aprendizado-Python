from random import randint


def maior(lista):
    print('-=' * 40)
    print('Analisando os valores passados...')
    mai = 0
    for c in lista:
        if mai == 0:
            mai = c
        elif c > mai:
            mai = c
        print(c, end=' ')
    print(f'Foram informador {len(lista)} valores ao todo')
    print(f'O maior valor informado foi {mai}')
    print('-=' * 40)


# Programa Principal
lis = list()
entrada = int(input('Quantos grupos de valores deseja analisar? '))
for c1 in range(0, entrada):
    numeros = randint(1, 10)
    for c2 in range(0, numeros):
        n = randint(1, 10)
        lis.append(n)
    maior(lis)
    lis.clear()
