abreParenteses = 0
fechaParenteses = 0
primeiro = False
expressao = str(input('Digite a expressão: '))

for c in expressao:
    if c in '(':
        break

    if c in ')':
        primeiro = True
        break

if not primeiro:
    for c in expressao:
        if c in '(':
            abreParenteses += 1

        if c in ')':
            fechaParenteses += 1

if primeiro or abreParenteses != fechaParenteses:
    print('A expressão está incorreta')
else:
    print('A expressão está correta')
