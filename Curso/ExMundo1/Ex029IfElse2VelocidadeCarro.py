v = float(input('Velocidade do carro: KmP/H '))
m = float

if v > 80:
    v = v - 80
    m = 7 * v
    print('Você estava {} kilometros acima da velocidade permitida, sua multa é de R${:.2f}!'.format(v, m))

else:
    print('Você está dentro da velocidade limite!')
