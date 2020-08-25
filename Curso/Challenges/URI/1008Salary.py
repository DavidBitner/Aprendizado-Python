employee_number = int(input())
hours_worked = int(input())
salary_per_hour = float(input())
salary_per_mounth = salary_per_hour * hours_worked
print("NUMBER = {}\nSALARY = U$ {:.2f}".format(employee_number, salary_per_mounth))
