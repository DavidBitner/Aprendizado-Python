n = 0
digitados = 0
soma = 0
while n != 999:
    n = int(input('Digite um numero: [999 para sair] '))
    if n == 999:
        n = 999
    else:
        digitados += 1
        soma += n
print('Você digitou {} numeros e a soma deles é {}'.format(digitados, soma))
