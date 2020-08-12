def linha():
    print('-' * 30)


def resumo(n, mais, menos):
    linha()
    print(f'{"RESUMO DO VALOR":^30}')
    linha()
    print(f'Preço analisado:    {moeda(n)}')
    print(f'Dobro do preço:     {moeda(dobro(n))}')
    print(f'Metade do preço:    {moeda(metade(n))}')
    print(f'{mais}% de aumento:     {moeda(aumentar(n, mais))}')
    print(f'{menos}% de redução:     {moeda(diminuir(n, menos))}')
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


def moeda(n):
    r = f'R${n:.2f}'
    return r
