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
for k, v in dicionario.items():
    print(f'    - {k} tem o valor {v}')
