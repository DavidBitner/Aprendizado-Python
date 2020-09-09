salary = float(input())
tax = answer = base = 0
if salary < 2000:
    print("Isento")
else:
    if salary <= 3000:
        salary -= 2000
        salary = salary * 8 / 100
    elif salary <= 4500:
        salary -= 2000
        base = salary - 1000
        base = base * 18 / 100
        base2 = 1000 * 8 / 100
        salary = base + base2
    elif salary > 4500:
        salary -= 2000
        base = salary - 2500
        base = base * 28 / 100
        base2 = 1000 * 8 / 100
        base3 = 1500 * 18 / 100
        salary = base + base2 + base3
    print(f"R$ {salary:.2f}")
