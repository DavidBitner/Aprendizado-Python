def dobro(n=0):
    r = n * 2
    return r


def metade(n=0):
    r = n / 2
    return r


def aumentar(n=0, a=0):
    r = n + (n * a / 100)
    return r


def diminuir(n=0, a=0):
    r = n - (n * a / 100)
    return r


def moeda(n=0, m='R$'):
    r = f'{m}{n:.2f}'.replace('.', ',')
    return r
