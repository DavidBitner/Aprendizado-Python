n = int(input())
a = b = c = base = 1
for i in range(0, n * 2):
    if i % 2 != 0:
        b += 1
        c += 1
    if i % 2 == 0:
        b = a * base
        c = a * b
        base += 1
    print(f"{a} {b} {c}")
    if i % 2 != 0:
        a += 1
