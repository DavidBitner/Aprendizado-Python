def leiaInt(numero):
    while True:
        numero = input('Digite um n: ')
        if numero.isnumeric():
            break
        else:
            print('ERRO! Digite um número inteiro válido.')

    return numero


# Programa Principal
n = leiaInt('Digite um n: ')
print(f'Você acabou de digitar o numero {n}')
