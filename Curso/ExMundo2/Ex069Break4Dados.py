mDezoito = hCadastrados = mVinte = 0
continuar = ' '

while True:
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [F/M/O]: ')).strip()
    print('-' * 20)
    if sexo not in 'FfMmOo':
        print('Sexo invalido, tente novamente!')
    else:
        if idade > 18:
            mDezoito += 1

        if sexo in 'Mm':
            hCadastrados += 1

        if sexo in 'Ff' and idade < 20:
            mVinte += 1

        while continuar not in 'SsNn':
            continuar = str(input('Deseja continuar? [S/N]: '))
            if continuar not in 'SsNn':
                print('Opção invalida, tente novamente!')
            else:
                break

        if continuar in 'Nn':
            print('\n\n')
            break

        continuar = ' '

print('====== FIM DO PROGRAMA ======')
print(f'{mDezoito} pessoas tem mais de 18 anos!')
print(f'{hCadastrados} homens foram cadastrados!')
print(f'{mVinte} mulheres tem menos de 20 anos!')
