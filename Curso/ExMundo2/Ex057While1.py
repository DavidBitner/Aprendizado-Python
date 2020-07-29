sexo = 'a'

while sexo not in 'mfo':
    sexo = str(input('Digite o sexo: [M/F/O]\n')).strip().lower()

if sexo == 'm':
    print('Sexo masculino registrado com sucesso')

elif sexo == 'o':
    print('Sexo outro registrado com sucesso')

else:
    print('Sexo feminino registrado com sucesso')
