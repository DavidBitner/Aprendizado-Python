n = int(input('Digite um numero: '))
opcao = int(input('Bem vindo ao conversor de numeros!\n1 - Conversão do numero para binário\n2 - Conversão do numero para octal\n3 - Conversão do numero para hexadecimal\n\nOpção: '))
if opcao == 1:
    bin = bin(n)
    print('O numero {} convertido para binário é {}'.format(n, bin[2:]))
elif opcao == 2:
    oct = oct(n)
    print('O numero {} convertido para binário é {}'.format(n, oct[2:]))
elif opcao == 3:
    hex = hex(n)
    print('O numero {} convertido para binário é {}'.format(n, hex[2:]))
else:
    print('Opção invalida')
