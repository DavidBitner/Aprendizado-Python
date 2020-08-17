frase = str(input('Digite uma frase: ')).strip().upper()

a = frase.count('A')
pa = frase.find('A') + 1
ua = frase.rfind('A') + 1

print('A frase digitada foi: {}'.format(frase))
print('A letra "A" aparece {} vezes'.format(frase, a))
print('A posição que a primeira letra "A" aparece na frase é a {}'.format(pa))
print('A posição que a ultima letra "A" aparece na frase é a {}'.format(ua))
