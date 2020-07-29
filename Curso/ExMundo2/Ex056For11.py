from datetime import datetime

bMedia = 0
media = 0

maisVelho = 0
mvBase = 0
hmVelho = 'Nenhuma das pessoas cadastradas foi homem, portanto nenhum homem é mais velho'

menosVinte = 0

for c in range(0, 4):
    nome = str(input('Digite o nome da {}º pessoa: '.format(c + 1))).strip().capitalize()
    anoNasc = int(input('Digite o ano de nascimento: '))
    sexo = str(input('Digite "M" para masculino, "F" para feminino e "O" para outro: ')).strip().lower()

    idade = datetime.today().year - anoNasc
    bMedia += idade

    maisVelho = datetime.today().year - anoNasc
    if sexo == 'm':
        if maisVelho > mvBase:
            hmVelho = nome
            mvBase = idade

    if sexo == 'f':
        if idade < 20:
            menosVinte += 1

media = bMedia / 4

print('A média de idade do grupo é de {:.1f} anos'.format(media))
print('O nome do homem mais velho é o {}'.format(hmVelho))
print('{} Mulher(es) tem menos de 20 anos'.format(menosVinte))
