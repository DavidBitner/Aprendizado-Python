import random

print('-=-' * 22)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
print('-=-' * 22)

n = int(input('Em que numero eu pensei? '))

r = random.randint(0, 5)

if n == r:
    print('Parabéns, você acertou o numero!')
else:
    print('Você errou o numero!')
