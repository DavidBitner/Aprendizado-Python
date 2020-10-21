n = input().split(' ')
a, b = float(n[0]), float(n[1])
diferenca = b - a
diferenca /= a
diferenca *= 100
print(f'{diferenca:.2f}%')
