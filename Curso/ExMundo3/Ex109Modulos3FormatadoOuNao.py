from ExMundo3 import Ex109Modulo

p = float(input('Digite o preço: R$'))
print(f'A metade de {Ex109Modulo.moeda(p)} é {Ex109Modulo.metade(p, True)}')
print(f'O dobro de {Ex109Modulo.moeda(p)} é {Ex109Modulo.dobro(p, True)}')
print(f'Aumentando 15%, temos {Ex109Modulo.aumentar(p, 15, True)}')
print(f'Diminuindo 20%, temos {Ex109Modulo.diminuir(p, 20, True)}')
