alcool = gasolina = diesel = 0
while True:
    codigo = int(input())
    if codigo == 4:
        break
    elif codigo == 1:
        alcool += 1
    elif codigo == 2:
        gasolina += 1
    elif codigo == 3:
        diesel += 1
print("MUITO OBRIGADO")
print(f"Alcool: {alcool}")
print(f"Gasolina: {gasolina}")
print(f"Diesel: {diesel}")
