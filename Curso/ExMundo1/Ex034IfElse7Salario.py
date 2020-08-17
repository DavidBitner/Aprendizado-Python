s = float(input('Digite o valor do salário: R$'))
a = float
sa = float
if s > 1250:
    a = s * 10 / 100
    sa = s + a
    print('O seu aumento foi de R${:.2f}, o seu novo salário é R${:.2f}'.format(a, sa))
else:
    a = s * 15 / 100
    sa = s + a
    print('O seu aumento foi de R${:.2f}, o seu novo salário é R${:.2f}'.format(a, sa))
