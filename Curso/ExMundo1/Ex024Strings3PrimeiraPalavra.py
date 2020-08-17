palavra = str(input('Digite o nome da cidade: ')).strip()
min = palavra.lower()
split = min.split()
primeirapalavra = split[0]
tf = 'santo' in primeirapalavra
print('A primeira palavra é SANTO?\n', tf)
