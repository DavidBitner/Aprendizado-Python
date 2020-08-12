from ExMundo3 import Ex107Modulo

p = float(input('Digite o preço: R$'))
print(f'A metade de {p} é {Ex107Modulo.metade(p)}')
print(f'O dobro de {p} é {Ex107Modulo.dobro(p)}')
print(f'Aumentando 15%, temos {Ex107Modulo.aumentar(p, 15):.2f}')
print(f'Diminuindo 20%, temos {Ex107Modulo.diminuir(p, 20):.2f}')
