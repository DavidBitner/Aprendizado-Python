person_age_in_days = int(input())
days = person_age_in_days % 30 // 2
temp = person_age_in_days // 30
months = temp % 12
temp = temp // 12
years = temp
print(f"{years} ano(s)")
print(f"{months} mes(es)")
print(f"{days} dia(s)")

INCOMPLETO
