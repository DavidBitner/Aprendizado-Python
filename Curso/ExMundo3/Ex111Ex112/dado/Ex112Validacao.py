def leiaDinheiro(numero):
    while True:
        numero = input('Digite o preço: R$')
        if numero.isnumeric():
            numero = int(numero)
            break
        else:
            print('ERRO! Digite um número inteiro válido.')

    return numero
