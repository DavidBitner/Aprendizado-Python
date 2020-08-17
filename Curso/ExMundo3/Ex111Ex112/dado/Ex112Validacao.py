def leiaDinheiro(msg):
    while True:
        numero = str(input(msg)).strip()
        if numero.isalpha() or numero == '':
            print('ERRO! Digite um preço válido.')
        else:
            if ',' in numero:
                numero = numero.replace(',', '.')
            numero = float(numero)
            break
    return numero
