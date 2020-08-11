from time import sleep


def bunitin(cor, txt):
    print(cor, end='')
    print(f'~' * (len(txt) + 4))
    print(f'  {txt}  ')
    print(f'~' * (len(txt) + 4))
    print('\033[m', end='')


# Programa Principal
while True:
    bunitin('\033[30;42;1m', 'SISTEMA DE AJUDA PyHELP')
    funcao = str(input('Função ou Biblioteca > ')).strip().lower()
    if funcao in 'fim':
        break
    bunitin('\033[30;44;1m', f"Acessando o manual do comando '{funcao}'")
    sleep(1)
    print('\033[7;30;1m', end='')
    help(funcao)
    print('\033[m', end='')
bunitin('\033[30;41;1m', 'ATÉ LOGO!')
