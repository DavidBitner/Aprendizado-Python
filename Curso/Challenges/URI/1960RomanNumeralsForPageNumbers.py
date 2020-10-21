n = int(input())
roman = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
normal = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
prt = ''
indice = 0
while n > 0:
    if n >= normal[indice]:
        prt += roman[indice]
        n -= normal[indice]
    else:
        indice += 1
print(prt)
