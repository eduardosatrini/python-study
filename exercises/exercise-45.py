# Total even numbers

total = 0
for i in range(1, 7):
    num = int(input("Type a number:"))
    if num % 2 == 0:
        total += num
print(f"Total: {total}")
