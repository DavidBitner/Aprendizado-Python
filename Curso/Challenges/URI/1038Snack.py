A, B = input().split(" ")
x, y = int(A), int(B)
total = float(0)
if x == 1:
    total = y * 4
elif x == 2:
    total = y * 4.50
elif x == 3:
    total = y * 5
elif x == 4:
    total = y * 2
elif x == 5:
    total = y * 1.50
print(f"Total: R$ {total:.2f}")
