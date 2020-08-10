def leiaInt(numero):
    while True:
        numero = input('Digite um n: ')
        if numero in '0123456789':
            break
        else:
            print('ERRO! Digite um número inteiro válido.')

    return numero


# Programa Principal
n = leiaInt('Digite um n: ')
