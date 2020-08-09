def areaRetangulo(largura, comprimento):
    area = largura * comprimento
    print(f'A área de um terreno {largura:.1f} X {comprimento:.1f} é de {area:.1f}m².')


# Programa principal
print('Controle de Terrenos')
print('-' * 30)
larg = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTO (m): '))
areaRetangulo(larg, comp)
