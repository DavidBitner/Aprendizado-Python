def linha():
    print('-' * 40)


def limpar():
    return print('\033[m', end='')


def verde():
    return print('\033[32m', end='')


def vermelho():
    return print('\033[31m', end='')


def menu():
    linha()
    print('MENU PRINCIPAL'.center(40))
    linha()
    while True:
        print(f'1 - Ver pessoas cadastradas')
        print(f'2 - Cadastrar nova Pessoa')
        print(f'3 - Sair do Sistema')
        linha()
        try:
            vermelho()
            opcao = int(input('Sua Opção: '))
            limpar()
            linha()
        except ValueError:
            limpar()
            linha()
            vermelho()
            print('ERRO! Você não digitou um numero!')
            limpar()
            linha()
        else:
            if opcao < 1 or opcao > 3:
                vermelho()
                print('ERRO! Numero Inválido!')
                limpar()
                linha()
            elif opcao == 1:
                listar()
                linha()
            elif opcao == 2:
                adicionar()
                linha()
            elif opcao == 3:
                linha()
                print('Saindo do sistema... Até logo!'.center(40))
                linha()
                break


def adicionar():
    print('ADICIONANDO NOVA PESSOA'.center(40))
    linha()
    txt = open('Ex115Modulo.txt', 'a+')
    nome = str(input('Digite o nome: ')).strip().capitalize()
    idade = leiaInt('Digite a idade: ')
    txt.write(f'{nome}'.ljust(30))
    txt.write(f'{idade} anos'.rjust(10))
    txt.write('\n')
    txt.close()


def listar():
    print('PESSOAS CADASTRADAS'.center(40))
    linha()
    txt = open('Ex115Modulo.txt', 'r')
    if txt.mode == 'r':
        conteudo = txt.read()
        print(conteudo)


def leiaInt(txt):
    while True:
        try:
            numero = int(input(txt))
        except ValueError:
            linha()
            vermelho()
            print('ERRO: por favor, digite um numero inteiro válido.')
            limpar()
            linha()
        else:
            break
    return numero
