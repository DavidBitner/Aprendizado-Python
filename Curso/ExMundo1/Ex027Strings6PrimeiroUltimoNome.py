nome = str(input('Digite um nome completo: ')).strip()
separado = nome.split()
pnome = separado[0]
unome = separado[-1]
print('O nome digitado foi: {}'.format(nome))
print('O primeiro nome é: {}'.format(pnome))
print('O ultimo nome é: {}'.format(unome))
