matriz = [[], [], []]
soma = 0
somaTerceira = 0
maior = 0

for cont1 in range(0, 3):
    for cont2 in range(0, 3):
        n = int(input(f'Digite um valor para [{cont1}, {cont2}]: '))
        matriz[cont1].append(n)
        if n % 2 == 0:
            soma += n

        if cont2 == 2:
            somaTerceira += n

        if cont1 == 1 and cont2 == 0:
            maior = n
        elif cont1 == 1 and n > maior:
            maior = n

print('-=' * 40)

for cont3 in range(0, 3):
    for cont4 in range(0, 3):
        print(f'[  {matriz[cont3][cont4]}  ]', end=' ')
    print()

print('-=' * 40)

print(f'A soma dos valores pares é {soma}')
print(f'A soma dos valores da terceira coluna é {somaTerceira}')
print(f'O maior valor da segunda linha é {maior}')
