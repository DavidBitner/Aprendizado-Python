i = 0
j = 1
base = j
while i <= 2:
    for c in range(0, 3):
        if i == 0 or i == 1 or 1.9 < i < 2:
            print(f"I={i:.0f} J={j:.0f}")
        else:
            print(f"I={i:.1f} J={j:.1f}")
        j += 1
    j = base
    j += 0.2
    i += 0.2
    base = j
