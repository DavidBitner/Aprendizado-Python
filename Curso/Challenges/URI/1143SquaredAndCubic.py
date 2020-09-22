n = int(input())
a = b = c = base = 1
for i in range(0, n):
    print(f"{a} {b} {c}")
    base += 1
    a += 1
    b = a * base
    c = a * b
