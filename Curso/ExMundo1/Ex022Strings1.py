p = str(input('Digite o seu nome completo: ')).strip()

maiu = p.upper()
minu = p.lower()

separado = p.split()
junto = ''.join(separado)
pnome = separado[0]

print('O nome com todas as letras maiúsculas é: {}'.format(maiu))
print('O nome com todas as letras minúsculas é: {}'.format(minu))
print('O nome contém {} caracteres ao todo sem espaços'.format(len(junto)))
print('O nome contém {} caracteres ao todo sem espaços'.format(len(p) - p.count(' ')))
print('O primeiro nome contém {} caracteres'.format(len(pnome)))
print('O primeiro nome contém {} caracteres'.format(p.find(' ')))
