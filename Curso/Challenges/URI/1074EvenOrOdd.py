entrada = int(input())
for i in range(0, entrada):
    number = int(input())
    if number == 0:
        print("NULL")
    else:
        if number % 2 == 0:
            print("EVEN", end=" ")
        else:
            print("ODD", end=" ")
        if number > 0:
            print("POSITIVE")
        else:
            print("NEGATIVE")
