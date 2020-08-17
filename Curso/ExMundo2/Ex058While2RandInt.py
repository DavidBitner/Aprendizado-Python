import random

print('-=-' * 22)
print('Vou pensar em um numero entre 0 e 10. Tente adivinhar...')
print('-=-' * 22)

n = int(input('Em que numero eu pensei? '))

r = random.randint(0, 10)

contador = 1

while n != r:
    if n > r:
        print('Você errou o numero, o numero que eu pensei é menor!')

    else:
        print('Você errou o numero, o numero que eu pensei é maior')

    n = int(input('Em que numero eu pensei? '))
    contador += 1

print('Parabéns você acertou!! Foram necessarias {} tentativas'.format(contador))
