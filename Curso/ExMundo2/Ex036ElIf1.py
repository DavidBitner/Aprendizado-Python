vcasa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o valor do salário: R$'))
anos = float(input('Digite a quantidade de anos de duração do pagamento do empréstimo: '))

mensalidade = vcasa / anos / 12
barreira = salario * 30 / 100

if  mensalidade > barreira:
    print('''Com o salário de R${:.2f} 
o empréstimo de R${:.2f} 
não poderá ser facilmente pago com a mensalidade de R${:.2f}, 
portanto o empréstimo é negado'''.format(salario, vcasa, mensalidade))

else:
    print('''Com o salário de R${:.2f} o empréstimo de R${:.2f} poderá ser pago com a mensalidade de R${:.2f}, portanto o empréstimo está aprovado!'''.format(salario, vcasa, mensalidade))
