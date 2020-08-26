spent_time = int(input())
average_speed = int(input())
distance = spent_time * average_speed
litters_needed = distance / 12
print("{:.3f}".format(litters_needed))
