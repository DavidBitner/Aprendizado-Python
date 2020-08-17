import math

n1 = float(input('Digite o numero do cateto oposto: '))
n2 = float(input('Digite o numero do cateto adjacente: '))

#n3 = n1**2 + n2**2
#h = sqrt(n3)

h = math.hypot(n1, n2)
print('A hipotenusa dos catetos {} e {} é {:.2f}'.format(n1, n2, h))
