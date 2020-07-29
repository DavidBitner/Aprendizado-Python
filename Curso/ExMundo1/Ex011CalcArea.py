lar = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))
area = lar * alt
tinta = area/2

print('A parede tem {:.3f} metros quadrados!'.format(area))
print('Serão necessários {:.4f} litros de tinta para pintar a parede'.format(tinta))
