import random

a1 = str(input('Digite o nome do primeiro aluno: '))
a2 = str(input('Digite o nome do segundo aluno: '))
a3 = str(input('Digite o nome do terceiro aluno: '))
a4 = str(input('Digite o nome do quarto aluno: '))
a5 = str(input('Digite o nome do quinto aluno: '))

lista = [a1, a2, a3, a4, a5]

random = random.choice(lista)

print('O aluno escolhido foi o {}!'.format(random))
