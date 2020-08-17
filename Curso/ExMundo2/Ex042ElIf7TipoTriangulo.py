r1 = float(input('Digite o valor da primeira reta: '))
r2 = float(input('Digite o valor da segunda reta: '))
r3 = float(input('Digite o valor da terceira reta: '))
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('Os valores {} {} {} formam um triângulo'.format(r1, r2, r3))
    if r1 == r2 == r3:
        print('E o triângulo é equilátero')
    elif r1 != r2 and r2 != r3 and r1 != r3:
        print('E o triângulo é escaleno')
    else:
        print('E o triângulo é Isósceles')
else:
    print('Os valores {} {} {} não formam um triângulo'.format(r1, r2, r3))
