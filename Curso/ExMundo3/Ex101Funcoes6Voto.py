def voto(ano):
    from datetime import datetime
    idade = datetime.today().year - ano
    if idade < 16:
        print(f'Com {idade} anos: NÃO VOTA')
    elif idade < 18 or idade > 65:
        print(f'Com {idade} anos: VOTO OPCIONAL')
    else:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO')


# Programa Principal
voto(int(input('Em que ano você nasceu? ')))
