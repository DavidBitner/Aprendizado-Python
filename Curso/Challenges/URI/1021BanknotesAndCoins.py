value = float(input())
notas100 = notas50 = notas20 = notas10 = notas5 = notas2 = moedas1 = moedas50 = moedas25 = moedas10 = moedas5 = moedas01 = 0
value += 0.001

while value >= 100:
    value -= 100
    notas100 += 1
while value >= 50:
    value -= 50
    notas50 += 1
while value >= 20:
    value -= 20
    notas20 += 1
while value >= 10:
    value -= 10
    notas10 += 1
while value >= 5:
    value -= 5
    notas5 += 1
while value >= 2:
    value -= 2
    notas2 += 1
while value >= 1:
    value -= 1
    moedas1 += 1
while value >= 0.50:
    value -= 0.50
    moedas50 += 1
while value >= 0.25:
    value -= 0.25
    moedas25 += 1
while value >= 0.10:
    value -= 0.10
    moedas10 += 1
while value >= 0.05:
    value -= 0.05
    moedas5 += 1
while value >= 0.01:
    value -= 0.01
    moedas01 += 1

print("NOTAS:")
print(f"{notas100} nota(s) de R$ 100.00")
print(f"{notas50} nota(s) de R$ 50.00")
print(f"{notas20} nota(s) de R$ 20.00")
print(f"{notas10} nota(s) de R$ 10.00")
print(f"{notas5} nota(s) de R$ 5.00")
print(f"{notas2} nota(s) de R$ 2.00")
print("MOEDAS:")
print(f"{moedas1} moeda(s) de R$ 1.00")
print(f"{moedas50} moeda(s) de R$ 0.50")
print(f"{moedas25} moeda(s) de R$ 0.25")
print(f"{moedas10} moeda(s) de R$ 0.10")
print(f"{moedas5} moeda(s) de R$ 0.05")
print(f"{moedas01} moeda(s) de R$ 0.01")
