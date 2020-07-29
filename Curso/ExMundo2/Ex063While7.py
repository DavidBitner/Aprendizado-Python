n = int(input('Digite o numero da sequencia de Fibonacci: '))

fa = 0
fb = 1
f = 1

print('0 > 1 > ', end='')

while n - 2 > 0:
    f = fa + fb
    fa = fb
    fb = f

    print(f, end=' > ')

    n -= 1
print('Fim')
