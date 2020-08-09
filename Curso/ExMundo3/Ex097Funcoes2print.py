def escreva(txt):
    print('~' * (len(txt) + 4))
    print(f'  {txt}  ')
    print('~' * (len(txt) + 4))


# Programa principal
escreva(str(input('Digite o texto: ')))
