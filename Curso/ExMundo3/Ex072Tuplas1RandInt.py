numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze,', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezesete', 'Dezoito', 'Dezenove', 'Vinte')
novamente = ' '
while True:
    entrada = int(input('Digite um numero entre 0 e 20: '))
    if entrada > 20 or entrada < 0:
        print('Tente novamente. ', end='')
    else:
        print(f'O numero {entrada} por extenso é {numeros[entrada]}')
        while True:
            novamente = str(input('Deseja tentar novamente? [S/N]')).strip().lower()
            if novamente not in 'sn':
                print('Invalido, tente novamente!')
            else:
                break
    if novamente in 'n':
        break
