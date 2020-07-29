import math

n = float(input('Digite um numero real: '))
print('O numero {} tem a parte inteira {}'.format(n, int(n)))
print('O numero {} tem a parte inteira {}'.format(n, math.trunc(n)))
