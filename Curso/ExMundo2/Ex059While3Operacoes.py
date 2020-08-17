from time import sleep

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

opcao = 0

while opcao != 5:
    opcao = int(input('''Escolha uma das opções:
    [1] Somar os dois numeros
    [2] Multiplicar os dois numeros
    [3] Saber qual dos numeros é maior
    [4] Digitar novos numeros
    [5] Sair do programa
    
    Opção: '''))
    print('\n')

    if opcao == 1:
        print('A soma dos dois numeros é: {}'.format(n1 + n2))
        sleep(3)

    elif opcao == 2:
        print('O produto dos dois numeros é: {}'.format(n1 * n2))
        sleep(3)

    elif opcao == 3:
        if n1 > n2:
            print('O primeiro numero: {} é maior que o segundo numero: {}'.format(n1, n2))
            sleep(3)

        elif n2 > n1:
            print('O segundo numero: {} é maior que o primeiro numero: {}'.format(n2, n1))
            sleep(3)

        else:
            print('Os valores {} e {} são iguais, portanto não há maior'.format(n1, n2))
            sleep(3)

    elif opcao == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))

    elif opcao == 5:
        print()

    else:
        print('Opção invalida, tente novamente!')
        sleep(3)
