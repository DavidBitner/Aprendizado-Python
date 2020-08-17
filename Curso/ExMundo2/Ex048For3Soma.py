s = 1
e = 500
p = 2
r = 0

for c in range(s, e, p):
    if c % 3 == 0:
        r = r + c

print(r)
