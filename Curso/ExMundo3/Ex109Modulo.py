def dobro(n, o=False):
    r = n * 2
    if o:
        r = f'R${r:.2f}'
    return r


def metade(n, o=False):
    r = n / 2
    if o:
        r = f'R${r:.2f}'
    return r


def aumentar(n, a, o=False):
    r = n + (n * a / 100)
    if o:
        r = f'R${r:.2f}'
    return r


def diminuir(n, a, o=False):
    r = n - (n * a / 100)
    if o:
        r = f'R${r:.2f}'
    return r


def moeda(n):
    r = f'R${n:.2f}'
    return r
