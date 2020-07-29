a = int(input('Digite o primeiro numero: '))
b = int(input('Digite o segundo numero: '))
c = int(input('Digite o terceiro numero: '))

if a > b and a > c:
    print('O primeiro numero "{}" é o maior'.format(a))

elif b > a and b > c:
    print('O segundo numero "{}" é o maior'.format(b))

elif c > a and c > b:
    print('O terceiro numero "{}" é o maior'.format(c))

else:
    print('Mais de um numero é igual, portanto não tem um maior dentre os três')
