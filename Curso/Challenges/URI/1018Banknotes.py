value = int(input())
print(value)
temp = value // 100
print("{} nota(s) de R$ 100,00".format(temp))
value = value % 100
temp = value // 50
print("{} nota(s) de R$ 50,00".format(temp))
value = value % 50
temp = value // 20
print("{} nota(s) de R$ 20,00".format(temp))
value = value % 20
temp = value // 10
print("{} nota(s) de R$ 10,00".format(temp))
value = value % 10
temp = value // 5
print("{} nota(s) de R$ 5,00".format(temp))
value = value % 5
temp = value // 2
print("{} nota(s) de R$ 2,00".format(temp))
value = value % 2
temp = value // 1
print("{} nota(s) de R$ 1,00".format(temp))
