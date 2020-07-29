a = int(input('Digite o ano de nascimento: '))

n = 2002 - a

if n < 0:
    n = n * -1
    print('Ainda faltam {} anos para o alistamento militar!'.format(n))

elif n > 0:

    print('Já se passaram {} anos para o alistamento militar!'.format(n))

else:
    print('Este é o ano para efetuar o alistamento militar!')
