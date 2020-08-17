string = str(input('Digite a frase ou palavra para checar se a mesma é um palindromo: ')).strip().lower()

junto = string.split()
frase = ''.join(junto)

inverso = ''

for letra in range(len(frase) - 1, -1, -1):
    inverso = inverso + frase[letra]

print('{} = Sua frase\n{} = Sua frase ao contrário'.format(frase, inverso))

if frase == inverso:
    print('A string é um palindromo')

else:
    print('A string não é um palindromo')