A, B, C = input().split(" ")
a, b, c = float(A), float(B), float(C)
rectangled_triangle = a * c / 2
circle = 3.14159 * c * c
trapezium = ((a + b) * c) / 2
square = b * b
rectangle = a * b
print("TRIANGULO: {:.3f}".format(rectangled_triangle))
print("CIRCULO: {:.3f}".format(circle))
print("TRAPEZIO: {:.3f}".format(trapezium))
print("QUADRADO: {:.3f}".format(square))
print("RETANGULO: {:.3f}".format(rectangle))
