A, B, C = input().split(" ")
a, b, c = float(A), float(B), float(C)
temp = 0
if a < b:
    temp = a
    a = b
    b = temp
if b < c:
    temp = b
    b = c
    c = temp
if a < b:
    temp = a
    a = b
    b = temp
if a >= b + c:
    print("NAO FORMA TRIANGULO")
else:
    if (a * a) == (b * b) + (c * c):
        print("TRIANGULO RETANGULO")
    else:
        if (a * a) > (b * b) + (c * c):
            print("TRIANGULO OBTUSANGULO")
        elif (a * a) < (b * b) + (c * c):
            print("TRIANGULO ACUTANGULO")
        if a == b == c:
            print("TRIANGULO EQUILATERO")
        if a == b:
            if a != c or b != c:
                print("TRIANGULO ISOSCELES")
        if a == c:
            if a != b or c != b:
                print("TRIANGULO ISOSCELES")
        if b == c:
            if b != a or c != a:
                print("TRIANGULO ISOSCELES")
