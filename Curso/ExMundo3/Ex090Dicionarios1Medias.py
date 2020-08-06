pessoas = dict()

pessoas['nome'] = str(input('Nome: '))
pessoas['media'] = float(input(f'Média de {pessoas["nome"]}: '))
if pessoas['media'] < 5:
    pessoas['situacao'] = 'Reprovado'
elif pessoas['media'] < 7:
    pessoas['situacao'] = 'Recuperação'
else:
    pessoas['situacao'] = 'Aprovado'

print(f'Nome é igual a {pessoas["nome"]}')
print(f'Média é igual a {pessoas["media"]:.1f}')
print(f'Situação é igual a {pessoas["situacao"]}')
