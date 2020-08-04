pessoas = list()
dados = list()
pesadas = list()
leves = list()
mPesada = mLeve = 0

while True:
    dados.append(str(input('Digite o nome: ')))
    dados.append(float(input('Digite o peso: ')))
    pessoas.append(dados[:])
    dados.clear()

    while True:
        continuar = str(input('Quer continuar? [S/N] ')).strip()

        if continuar in 'SsNn':
            break

    if continuar in 'Nn':
        break

for c in range(0, len(pessoas)):
    if c == 0:
        pesadas.append(pessoas[c][0])
        mPesada = pessoas[c][1]
    elif pessoas[c][1] == mPesada:
        pesadas.append(pessoas[c][0])
    elif pessoas[c][1] > mPesada:
        pesadas.clear()
        pesadas.append(pessoas[c][0])
        mPesada = pessoas[c][1]

    if c == 0:
        leves.append(pessoas[c][0])
        mLeve = pessoas[c][1]
    elif pessoas[c][1] == mLeve:
        leves.append(pessoas[c][0])
    elif pessoas[c][1] < mLeve:
        leves.clear()
        leves.append(pessoas[c][0])
        mLeve = pessoas[c][1]

print(f'{len(pessoas)} pessoas foram cadastradas')
print(f'O maior peso foi de {mPesada:.2f}. Peso de {pesadas}')
print(f'O menor peso foi de {mLeve:.2f}. Peso de {leves}')
