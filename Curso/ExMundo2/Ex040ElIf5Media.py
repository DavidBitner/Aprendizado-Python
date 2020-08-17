n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
if m >= 7:
    print('Sua média é {:.1f} e portanto você está aprovado'.format(m))
elif m < 5:
    print('Sua média é {:.1f} e portanto você está reprovado'.format(m))
else:
    print('Sua média é {:.1f} e portanto você está de recuperação'.format(m))
