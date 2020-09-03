A, B = input().split(" ")
a, b = int(A), int(B)
if b % a == 0:
    print("Sao Multiplos")
elif a % b == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
