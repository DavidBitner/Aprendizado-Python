s = 1
e = 11
p = 1

n = int(input('Digite o numero para tabuada: '))
r = 0
for c in range(s, e, p):
    r = n * c
    print('O numero {} X {:2} = {:2}'.format(n, c, r))
