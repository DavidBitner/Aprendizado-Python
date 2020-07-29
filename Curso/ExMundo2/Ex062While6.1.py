base = 1
opcao = 1

while opcao != 0:

    primeiroTermo = int(input('Digite o primeiro termo da PA: '))
    razao = int(input('Digite a razão da PA: '))
    opcao = int(input('Quantos termos da PA devem ser mostrados? (Digite "0" para finalizar) '))
    show = primeiroTermo

    if opcao != 0:
        base = opcao
        while base > 0:
            print(show, end=' > ')
            show = primeiroTermo + razao
            primeiroTermo = show
            base -= 1
        print('Fim')
