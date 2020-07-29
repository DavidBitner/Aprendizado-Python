base = 1
opcao = 1
mostrados = 0

primeiroTermo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

while opcao != 0:

    opcao = int(input('Mais quantos termos da PA devem ser mostrados? (Digite "0" para finalizar) '))
    show = primeiroTermo

    if opcao != 0:
        base = opcao
        while base > 0:
            print(show, end=' > ')
            show = primeiroTermo + razao
            primeiroTermo = show
            base -= 1
            mostrados += 1
        print('PAUSA')

print('\n\033[4mProgressão finalizada com {} termos mostrados'.format(mostrados))
