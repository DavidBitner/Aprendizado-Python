employee_salary = float(input())
readjustment_rate = gain = 0
if 0 <= employee_salary <= 400:
    readjustment_rate = 15
elif 400 < employee_salary <= 800:
    readjustment_rate = 12
elif 800 < employee_salary <= 1200:
    readjustment_rate = 10
elif 1200 < employee_salary <= 2000:
    readjustment_rate = 7
elif 2000 < employee_salary:
    readjustment_rate = 4
gain = employee_salary * readjustment_rate / 100
employee_salary = employee_salary + (employee_salary * readjustment_rate / 100)
print(f"Novo salario: {employee_salary:.2f}")
print(f"Reajuste ganho: {gain:.2f}")
print(f"Em percentual: {readjustment_rate} %")
