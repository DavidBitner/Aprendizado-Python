d = int(input('Digite a distância percorrida: Km '))
p = float
if d <= 200:
    p = d * 0.50
    print('Total a pagar pelos {}Km rodados é R${:.2f}'.format(d, p))
else:
    p = d * 0.45
    print('Total a pagar pelos {}Km rodados é R${:.2f}'.format(d, p))
