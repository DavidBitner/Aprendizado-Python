base = 10

primeiroTermo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
show = primeiroTermo

while base > 0:
    print(show, end=' > ')
    show = primeiroTermo + razao
    primeiroTermo = show
    base -= 1
print('Fim')
