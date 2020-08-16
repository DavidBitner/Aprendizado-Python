def leiaInt(txt):
    while True:
        try:
            numero = int(input(txt))
        except ValueError:
            print('ERRO: por favor, digite um numero inteiro válido.')
        else:
            break
    return numero


def leiaFloat(txt):
    while True:
        try:
            numero = float(input(txt))
        except Exception:
            print('ERRO: por favor, digite um numero Float válido.')
        else:
            break
    return numero


# Programa Principal
i = leiaInt('Digite um numero inteiro: ')
print(f'Você acabou de digitar o numero {i}')
f = leiaFloat('Digite um numero float: ')
print(f'Você acabou de digitar o float {f}')
