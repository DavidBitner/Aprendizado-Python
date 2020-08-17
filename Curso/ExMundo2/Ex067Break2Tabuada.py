while True:
    n = int(input('Digite o numero da tabuada [0 para parar]: '))

    if n <= 0:
        break

    for c in range(0, 10):
        print(f'{n:1} X {c + 1:2} = {n * (c + 1):2}')
