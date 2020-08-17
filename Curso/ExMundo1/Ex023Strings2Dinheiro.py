numero = int(input('Digite um numero: '))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10
print('Milhar = {}\nCentena = {}\nDezena = {}\nUnidade = {}'.format(milhar, centena, dezena, unidade))

