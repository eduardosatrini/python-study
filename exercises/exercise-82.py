# show even and odd numbers just one list
values = [[], []]

for i in range(0, 6):
    value = int(input(f"Enter a {i+1}º value: "))

    if value % 2 == 0:
        values[0].append(value)
    else:
        values[1].append(value)        
print(f"Even values: {sorted(values[0])}")
print(f"Odd values: {sorted(values[1])}")
    
