n = float(input('Digite o salário: R$'))
print('Com o aumento de 15% o seu salário agora é R${:.2f}!'.format(n*1.15))
print('Você recebeu R${:.2f} de aumento'.format(n*0.15))

print('Aumento de R${:.2f}, novo salário R${:.2f}'.format(n * 15 / 100, n + (n * 15 / 100)))
