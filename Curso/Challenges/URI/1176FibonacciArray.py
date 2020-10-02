fib = []
f1 = 0
f2 = 1
f3 = 0
for i in range(0, 61):
    if i == 0:
        fib.append(f1)
        f1 = 1
    elif i == 1:
        fib.append(f2)
        f2 = 0
    else:
        f3 = f1 + f2
        f2 = f1
        f1 = f3
        fib.append(f3)
n = int(input())
for i in range(0, n):
    l = int(input())
    print(f"Fib({l}) = {fib[l]}")
