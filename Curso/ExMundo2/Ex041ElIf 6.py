a = int(input('Digite o ano de nascimento: '))

i = 2020 - a

if i <= 9:
    print('A categoria é mirim')

elif 14 >= i > 9:
    print('A categoria é infantil')

elif 19 >= i > 14:
    print('A categoria é junior')

elif 20 >= i > 19:
    print('A categoria é senior')

else:
    print('A categoria é master')
