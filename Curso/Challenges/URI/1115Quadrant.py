while True:
    A, B = input().split(" ")
    x, y = int(A), int(B)
    if x > 0 and y > 0:
        print("primeiro")
    elif x < 0 < y:
        print("segundo")
    elif x < 0 and y < 0:
        print("terceiro")
    elif x > 0 > y:
        print("quarto")
    else:
        break
