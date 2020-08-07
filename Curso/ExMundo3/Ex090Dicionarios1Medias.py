pessoas = dict()

pessoas['nome'] = str(input('Nome: '))
pessoas['media'] = float(input(f'Média de {pessoas["nome"]}: '))
if pessoas['media'] < 5:
    pessoas['situacao'] = 'Reprovado'
elif pessoas['media'] < 7:
    pessoas['situacao'] = 'Recuperação'
else:
    pessoas['situacao'] = 'Aprovado'

for k, v in pessoas.items():
    print(f'{k} é igual a {v}')
