seller_name = str(input())
salary = float(input())
sales_made = float(input())
bonus = sales_made * 15 / 100
total_salary = salary + bonus
print("TOTAL = R$ {:.2f}".format(total_salary))
