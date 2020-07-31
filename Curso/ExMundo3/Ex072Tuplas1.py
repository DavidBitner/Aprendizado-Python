numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze,', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezesete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    entrada = int(input('Digite um numero entre 0 e 20: '))
    if entrada > 20 or entrada < 0:
        print('Tente novamente. ', end='')
    else:
        break

print(f'O numero {entrada} por extenso é {numeros[entrada]}')
