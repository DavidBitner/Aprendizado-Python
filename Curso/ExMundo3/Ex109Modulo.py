def dobro(n, o=False):
    r = n * 2
    if o:
        r = moeda(r)
    return r


def metade(n, o=False):
    r = n / 2
    if o:
        r = moeda(r)
    return r


def aumentar(n, a, o=False):
    r = n + (n * a / 100)
    if o:
        r = moeda(r)
    return r


def diminuir(n, a, o=False):
    r = n - (n * a / 100)
    if o:
        r = moeda(r)
    return r


def moeda(n, m='R$'):
    r = f'{m}{n:.2f}'.replace('.', ',')
    return r
