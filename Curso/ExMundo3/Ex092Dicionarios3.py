from datetime import datetime

dicionario = dict()

dicionario['nome'] = str(input('Nome: ')).strip().capitalize()
nascimento = int(input('Ano de Nascimento: '))
dicionario['idade'] = datetime.today().year - nascimento
dicionario['carteira'] = int(input('Carteira de Trabalho (0 não tem): '))
if dicionario['carteira'] > 0:
    dicionario['contratacao'] = int(input('Ano de contratação: '))
    dicionario['salario'] = float(input('Salário: R$'))
    dicionario['aposentadoria'] = dicionario['contratacao'] - nascimento + 35

print(dicionario)
print(f'nome tem o valor {dicionario["nome"]}')
print(f'idade tem o valor {dicionario["idade"]}')
print(f'ctps tem o valor {dicionario["carteira"]}')
if dicionario['carteira'] > 0:
    print(f'contratação tem o valor {dicionario["contratacao"]}')
    print(f'salario tem o valor {dicionario["salario"]}')
    print(f'aposentadoria tem o valor {dicionario["aposentadoria"]}')
