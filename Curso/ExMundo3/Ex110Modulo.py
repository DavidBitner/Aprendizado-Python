def linha():
    print('-' * 30)


def resumo(n, mais, menos):
    linha()
    print('RESUMO DO VALOR'.center(30))
    linha()
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Dobro do preço: \t{moeda(dobro(n))}')
    print(f'Metade do preço: \t{moeda(metade(n))}')
    print(f'{mais}% de aumento: \t{moeda(aumentar(n, mais))}')
    print(f'{menos}% de redução: \t{moeda(diminuir(n, menos))}')
    linha()


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


def moeda(n, m='R$'):
    r = f'{m}{n:.2f}'.replace('.', ',')
    return r
