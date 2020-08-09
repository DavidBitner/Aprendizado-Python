from random import randint


def sorteia():
    lista = list()
    print(f'Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        n = randint(1, 10)
        print(n, end=' ')
        lista.append(n)
    print('PRONTO!')
    return lista


def somaPar(lista):
    soma = 0
    print(f'Somando os valores pares de {lista}, temos ', end='')
    for c in lista:
        if c % 2 == 0:
            soma += c
    print(soma)


# Programa Principal
l = sorteia()
somaPar(l)
