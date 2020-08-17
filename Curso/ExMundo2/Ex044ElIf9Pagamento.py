pn = float(input('Digite o preço do produto: R$'))
p = float
o = int(input('''Bem vindo! Escolha uma opção:
1 - À vista no dinheiro ou cheque
2 - À vista no cartão
3 - Em até 2x no cartão
4 - 3x ou mais no cartão

Opção: '''))

if o == 1:
    p = pn - (pn * 10 / 100)

elif o == 2:
    p = pn - (pn * 5 / 100)

elif o == 3:
    p = pn

elif o == 4:
    p = pn + (pn * 20 / 100)

else:
    print('Opção invalida')

print('O valor a pagar é R${:.2f}'.format(p))
