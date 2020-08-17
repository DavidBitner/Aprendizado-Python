n = float(input('Digite o valor do produto: R$'))
print('O valor do produto com 5% de desconto é R${:.2f}!'.format(n*0.95))
print('O valor do desconto é de R${:.2f}!'.format(n*0.05))
print('O valor de R${:.2f} com o desconto de 5% R${:.2f} se torna R${:.2f}'.format(n, n * 5 / 100, n - (n * 5 / 100)))
