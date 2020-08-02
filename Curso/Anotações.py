"""
1- () Primeiro se resolve o que está entre parenteses
2- ** Em seguida se resolve a potenciação
3- * / // % Depois se resolvem multiplação, divisão, divisão inteira e resto
4- + - E por ultimo são resolvidas as adições e subtrações

 5 + 3 * 2 == 11
 3 * 5 + 4 ** 2 == 31
 3 * (5 + 4) ** 2 == 243

 Raiz quadrada pode ser feita fazendo o numero ser a potência de meio
 Exemplo: A Raiz quadrada de 81 é 9, ou seja 81 com potência a meio é 9, ou seja 81 ** (1/2) == 9

 + - * / ** potência // Divisão inteira % Resto
 {:.3f} três casas decimais
 , end=' ' finaliza sem pular linha
 \n quebra linha
 Porcentagens podem ser calculadas da seguinte forma: valor * porcentagem / 100
 Para conseguir o valor menos a porcentagem: valor - (valor * porcentagem / 100)

"""

nome = input('Qual o seu nome?')
print('Doidera em {}!'.format(nome))
print('Doidera em {:20}!'.format(nome))
print('Doidera em {:>20}!'.format(nome))
print('Doidera em {:<20}!'.format(nome))
print('Doidera em {:^20}!'.format(nome))
print('Doidera em {:=^20}!'.format(nome))
print(f'Doidera em {nome:=^20}!')
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'{"FIM DO PROGRAMA":-^40}')

"""
import math
raiz = math.sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, raiz))
print('A raiz de {} é igual a {:.2f}'.format(num, maath.ceil(raiz)))
from math import sqrt, floor
raiz = sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, floor(raiz))

math.trunc = Cortar um numero real

frase[9] = Décimo caractere
frase[9:13] = Décimo caractere até décimo segundo
frase[9:21:2] = Mostrar os caracteres desde o 10 até o 20 pulando de 2 em 2
frase[:5] = Mostrar os caracteres desde o primeiro (ou o caractere 0) até o quinto caractere ou o caractere 4 dentro da lista
frase[15:] = Mostrar a frase a partir do caractere 16
frase[9::3] = Começar a mostrar a frase a partir do décimo caractere, até o final da frase, pulando de 3 em 3
len(frase) = Comprimento em caracteres da frase
frase.count('o') = Contar a quantidade de letras "o" na frase
frase.count('o',0,13) = Contar a quantidade de "o" na frase, levando em conta apenas os primeiros 13 caracteres (0>12)
frase.find('deo') = Achar dentro da frase a posição que se inicia "deo" (caso seja colocado um valor que não existe dentro da frase, o programa retornará o valor -1)
'Curso' in frase = Dizer se existe ou não a palavra "Curso" dentro de frase
frase.replace('Python','Android') Vai substituir dentro de frase o que for "Python" e colocar no lugar "Android"
frase.upper() = Mudar todas as letras minusculas em frase e transforma-las em maiusculas
frase.lower() = contrário de upper
frase.capitalize() = Vai colocar toda a string frase em minuscula e deixar apenas a primeira letra maiuscula
frase.title() = Vai separar toda a frase por palavras, e vai deixar com letra maiuscula todos os inicios das palavras
frase.strip() = Remover todos os espaços inuteis da string no começo e no fim dela
frase.rstrip() = Vai remover todos os espaços inuteis a direita da string
frase.lstrip() = Vai remover todos os espaços inuteis a esquerda da string
frase.split() = Dividir a string pelos espaços contidos dentro dela
'-'.join(frase) = Pegar uma string separada e vai junta-la usando como caractere divisor o "-"
print(frase.upper().count('O')) = Colocar toda a string frase em letra maiuscula, contar quantas letras "O" tem nessa frase, e mostrar na tela o numero de letras "O"
frase = frase.replace('Python', 'Andoid') = Mudar na string frase a palavra Python para Android
print(dividido[2]) = Mostrar dentro da lista "dividido" a palavra na posição 2 da lista

if sadlkfjnflksda():
    dsfasfd
else:
    okihnjkoi

print('carro novo' if tempo <=3 else 'carro velho')

import time
sleep (3) serve para fazer o computador pausar a execução durante 3 segundos

import date
ano = date.today().year = Vai atribuir a variável "ano" o ano atual

\033[0;33;44m padrão para cores no terminal
print('\033[4;30;45mOlá, Mundo!\033[m')

elif nome in 'Ana Cláudia Jéssica Juliana': = Identificar um dos nomes na lista

for c in range(1,10):
for c in range(0, 7, 2):
for c in range(0, 7, -1):
for c in range(0, n):
for c in lista: = percorre uma lista

while condição:
while not condição:

variavel = false
while not variavel: = enquanto a variavel não se tornar verdadeira, o laço continuará rodando


exemplo = () = Tupla
exemplo = [] = Lista
exemplo = {} = Dicionário

Importante: Tuplas são imutáveis
exemplo = ('Primeiro', 'Segundo', 'Terceiro', 'Quarto')
print(exemplo[2]) = printar dentro da tupla o que estiver alocado na posição 3
print(exemplo[0:2]) = printar dentro da tupla o que estiver alocado entre as posições 1 e 2
print(exemplo[1:]) = printar dentro da tupla o que estiver alocado a partir da posição 2 até o final
print(exemplo[-1]) = printar dentro da tupla o ultimo valor existente nela
print(sorted(exemplo)) = Printar a tupla completa em ordem alfabetica
len(exemplo) = Mostrar a quantidade de valores alocados dentro da tupla "exemplo"


for c in exemplo:
    print(c)
= Printar tudo que estiver dentro da tupla, um por um

for c in range(0, len(exemplo)): 
    print(exemplo[c])    
= Mostrar o que estiver dentro da tupla "Exemplo" desde a posição 0

a = (2, 4, 6) = Primeira tupla
b = (1, 4, 5, 7) = Segunda tupla
c = a + b = Terceira tupla composta das duas primeiras tuplas
print(c.count(4)) = Mostrar quantas vezes o numero 4 aparece dentro da tupla "c"
print(c.index(7)) = Mostrar em que posição dentro da tupla o "7" se encontra

tupla = (randint(0, 10), randint(0, 10)) = Randomizar dois numeros e colocalos numa tupla

max(tupla) = Maior numero dentro de uma sequencia de numeros
min(tupla) = Menor numero dentro de uma sequencia de numeros

tupla = (str(input('Digite aqui')), str(input('Digite aqui')))
= Popular uma tupla com entradas do usuário


lista.append('Exemplo') = Adicionar um valor a lista
lista.insert(0, 'Exemplo') = Adicionar a primeira posição da lista o valor "Exemplo"
del lista[3] = Deletar da lista o quarto valor dela
lista.pop[3] = Deletar da lista o quarto valor dela
lista.pop() = Deletar o ultimo valor da lista
lista.remove('Exemplo') = Deletar da lista o valor "Exemplo"
lista = list(range(4, 11)) = Criar uma lista com os valor de 4 até 10
lista.sort() = Alterar a lista para que os valores fiquem na ordem
lista.sort(reverse=True) = Alterar a lista para que os valores fiquem na ordem, de trás para frente
len(lista) = Mostrar o numero de valores dentro da lista

for c, v in enumerate(lista):
    print(f'Na posição {c} encontrei o valor {v}!')
= mostrar a lista e a posição do valor dentro da lista

for c in range(0,5):
    lista.append(int(input('Digite um valor:')))
= Usuário popular uma lista com cinco valores

listaA = [1, 2, 3, 4] = Lista A
listaB = listaA = Conexão entre lista A e B
listaB = listaA[:] = Cópia da lista A
"""

print('\033[4;30;45mOlá, Mundo!\033[m')
print('Olá {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))

