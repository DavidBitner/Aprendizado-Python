total = 0
soma = 0

while True:
    n = int(input('Digite um numero [999 para parar]: '))

    if n == 999:
        break

    total += 1
    soma += n

print(f'Foram digitados {total} numeros!')
print(f'A soma dos numeros digitados é {soma}')
