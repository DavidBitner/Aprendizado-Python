from ExMundo3 import Ex108Modulo

p = float(input('Digite o preço: R$'))
print(f'A metade de {Ex108Modulo.moeda(p)} é {Ex108Modulo.moeda(Ex108Modulo.metade(p))}')
print(f'O dobro de {Ex108Modulo.moeda(p)} é {Ex108Modulo.moeda(Ex108Modulo.dobro(p))}')
print(f'Aumentando 15%, temos {Ex108Modulo.moeda(Ex108Modulo.aumentar(p, 15))}')
print(f'Diminuindo 20%, temos {Ex108Modulo.moeda(Ex108Modulo.diminuir(p, 20))}')
