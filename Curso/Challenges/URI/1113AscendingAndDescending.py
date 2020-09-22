while True:
    A, B = input().split(" ")
    x, y = int(A), int(B)
    if x > y:
        print("Decrescente")
    elif y > x:
        print("Crescente")
    else:
        break
