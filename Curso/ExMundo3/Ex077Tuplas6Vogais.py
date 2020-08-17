palavras = ('Doidera', 'Calipso', 'Yoda', 'Axt', 'Jovirone', 'Matilda', 'Schwarzenneger', 'Mustefaga', 'Instinct', 'Kobayashi', 'Ludgero', 'Salcicha', 'Scooby', 'Turtle', 'Lily', 'Toast')
for palavra in palavras:
    print(f'Na palavra {palavra.upper()} temos ', end='')
    for c in range(0, len(palavra)):
        if palavra[c] in 'AaEeIiOoUu':
            print(palavra[c].lower(), end=' ')
    print()
