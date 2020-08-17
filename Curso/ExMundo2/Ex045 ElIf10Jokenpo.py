from random import choice
c = choice(['PEDRA', 'PAPEL', 'TESOURA'])
print('U_U'*7)
print('Vamos jogar JOKENPO!')
print('U_U'*7)
h = str(input('Digite "Pedra", "Papel" ou "Tesoura": ')).strip().upper()
if h == 'PEDRA' or h == 'TESOURA' or h == 'PAPEL':
    print('Eu escolhi {} e você escolheu {}\n'.format(c, h))
    if c == 'PEDRA' and h == 'PAPEL' or c == 'PAPEL' and h == 'TESOURA' or c == 'TESOURA' and h == 'PEDRA':
        print('Você ganhou')
    elif c == 'PEDRA' and h == 'TESOURA' or c == 'TESOURA' and h == 'PAPEL' or c == 'PAPEL' and h == 'PEDRA':
        print('GANHEI ' * 10)
    else:
        print('Empatamos')
else:
    print('\nOpção invalida! Ganhei')
