while True:
    try:
        maior = 0
        n = int(input())
        slugs = input().split(" ")
        for i in range(0, len(slugs)):
            if int(slugs[i]) > maior:
                maior = int(slugs[i])
        if maior < 10:
            print(1)
        elif 10 <= maior < 20:
            print(2)
        elif maior >= 20:
            print(3)
    except EOFError:
        break
