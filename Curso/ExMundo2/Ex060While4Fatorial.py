n = int(input('Digite um numero: '))
base = n-1
resposta = n
print('{}! = {} X '.format(n, n), end='')
while base > 0:
    resposta = resposta * base
    if base > 1:
        print('{} X '.format(base), end='')
    else:
        print(end='1')
    base -= 1
print(' = {}'.format(resposta))
print('O fatorial do numero {} é {}'.format(n, resposta))
