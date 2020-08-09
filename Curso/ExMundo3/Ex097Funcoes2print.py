def escreva(txt):
    print('~' * (len(txt) + 4))
    print(f'  {txt}  ')
    print('~' * (len(txt) + 4))


# Programa principal
t = str(input('Digite o texto: '))
escreva(t)
