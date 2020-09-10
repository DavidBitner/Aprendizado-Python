person_age_in_days = int(input())
years = person_age_in_days // 365
temp = person_age_in_days % 365
months = temp // 30
temp = temp % 30
days = temp
print(f"{years} ano(s)")
print(f"{months} mes(es)")
print(f"{days} dia(s)")
