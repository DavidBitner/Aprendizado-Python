'''
numero = int(input('Digite um numero entre 0 e 9999: '))

numerostring = str(numero)

unidade = numerostring[3]
dezena = numerostring[2]
centena = numerostring[1]
milhar = numerostring[0]

print('Milhar = {}\nCentena = {}\nDezena = {}\nUnidade = {}'.format(milhar, centena, dezena, unidade))
'''


numero = int(input('Digite um numero: '))

unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10

print('Milhar = {}\nCentena = {}\nDezena = {}\nUnidade = {}'.format(milhar, centena, dezena, unidade))

