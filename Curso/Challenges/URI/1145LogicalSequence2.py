A, B = input().split(" ")
x, y = int(A), int(B)
base = 1
for i in range(1, y + 1):
    print(f"{i}", end="")
    if base != x:
        print(" ", end="")
    if base == x:
        print()
        base = 0
    base += 1
