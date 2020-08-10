def fatorial(numero, opcao=False):
    """
    Função para calcular o fatorial de um numero
    :param numero: Numero a ser calculado
    :param opcao: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um numero n.
    """
    base = numero - 1
    resposta = numero
    if opcao:
        print(f'{numero}! = {numero} X ', end='')
    while base > 0:
        resposta = resposta * base
        if opcao:
            if base > 1:
                print(f'{base} X ', end='')
            else:
                print(end='1')
        base -= 1
    if opcao:
        print(f' = {resposta}')
    print(f'O fatorial do numero {numero} é {resposta}')


# Programa Principal
n = int(input('Digite um numero: '))
o = bool()
while True:
    entrada = int(input('Deseja ver a conta do numero fatorial? [1-sim/2-não] '))
    if entrada == 1:
        o = True
        break
    elif entrada == 2:
        break
fatorial(n, o)
