from time import sleep


def contagem(inicio, fim, passo):
    print('-=' * 20)
    if passo > 0:
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
        fim += 1
    elif passo < 0:
        print(f'Contagem de {inicio} até {fim} de {passo * -1} em {passo * -1}')
        fim -= 1

    for c in range(inicio, fim, passo):
        print(c, end=' ')
        sleep(0.3)
    print('FIM!')
    print('-=' * 20)


# Programa Principal
contagem(1, 10, 1)
contagem(10, 0, -2)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
if i > f:
    p = p * -1
contagem(i, f, p)
