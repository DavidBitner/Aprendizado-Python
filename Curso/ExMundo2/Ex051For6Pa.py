s = 0
e = 10
p = 1

primeiroTermo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
show = primeiroTermo

for c in range(s, e, p):
    print(show, end=' > ')
    show = primeiroTermo + razao
    primeiroTermo = show
print('Fim')
