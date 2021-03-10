# Matriz in python
numbers = [[], [], []]

for i in range(0, 3):
    for c in range(0, 3):
        value = int(input(f"Enter a value [{i}, {c}]: "))
        numbers[i].append(value)
for lists in numbers:
    for i in lists:
        print(f"( {i:^5} )", end = "")
    print()
print("Program end..")
