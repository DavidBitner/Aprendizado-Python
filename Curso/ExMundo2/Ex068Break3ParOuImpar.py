from random import randint

vitoria = 0
while True:
    maquina = randint(0, 10)
    humanoEscolha = str(input('Par ou Impar? [P/I]: ')).strip()
    if humanoEscolha not in 'PpIi':
        print('OPÇÃO INVALIDA, TENTE NOVAMENTE')
    else:
        humanoNumero = int(input('Escolha um numero: '))
        resultado = humanoNumero + maquina
        if resultado % 2 == 0:
            print('-' * 20)
            print(f'Você jogou {humanoNumero} e o computador {maquina}. Total de {resultado} DEU PAR')
            print('-' * 20)
        else:
            print('-' * 20)
            print(f'Você jogou {humanoNumero} e o computador {maquina}. Total de {resultado} DEU IMPAR')
            print('-' * 20)
        if humanoEscolha in 'Pp':
            if resultado % 2 == 0:
                print('Você VENCEU!')
                print('Vamos jogar novamente...')
                print('=-' * 10)
                vitoria += 1
            else:
                print('Você PERDEU!')
                print('=-' * 10)
                break
        elif humanoEscolha in 'Ii':
            if resultado % 2 != 0:
                print('Você VENCEU')
                print('Vamos jogar novamente...')
                print('-' * 20)
                vitoria += 1
            else:
                print('Você PERDEU!')
                print('=-' * 10)
                break
print(f'GAME OVER! Você venceu {vitoria} vezes')
