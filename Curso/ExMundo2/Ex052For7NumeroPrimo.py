inp = int(input('Digite um numero para saber se este é primo: '))
s = 1
e = inp + 1
p = 1
tf = 0
for c in range(s, e, p):
    if inp % c == 0:
        tf = tf + 1
        print('\033[33m', end=' ')
    else:
        print('\033[31m', end=' ')
    print(c, end='')
print('\033[m')
if tf != 2:
    print('\nO numero não é primo')
else:
    print('\nO numero é primo')
