duration_seconds = int(input())
seconds = duration_seconds % 60
temp = duration_seconds // 60
minutes = temp % 60
temp = temp // 60
hours = temp % 60
print(f"{hours}:{minutes}:{seconds}")
