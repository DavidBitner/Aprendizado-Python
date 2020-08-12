def dobro(n):
    r = n * 2
    return r


def metade(n):
    r = n / 2
    return r


def aumentar(n, a):
    r = n + (n * a / 100)
    return r


def diminuir(n, a):
    r = n - (n * a / 100)
    return r


def moeda(n):
    r = f'R${n:.2f}'
    return r
