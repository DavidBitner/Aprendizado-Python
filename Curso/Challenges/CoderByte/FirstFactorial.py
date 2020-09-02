def FirstFactorial(num):
    base = num - 1
    while base > 1:
        num *= base
        base -= 1
    return num


# Main
print(FirstFactorial(int(input())))
