from datetime import datetime

menores = 0
maiores = 0
idade = 0
anoAtual = datetime.today().year
for c in range(0, 6):
    ano = int(input('Em que ano a {}º pessoa nasceu? '.format(c + 1)))
    idade = anoAtual - ano
    if idade >= 18:
        maiores += 1
    else:
        menores += 1
print('{} pessoas são menores de idade e {} são maiores de idade'.format(menores, maiores))
