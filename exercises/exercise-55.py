num = int(input("Calculate factorial: !"))
factorial = 1
for i in range(num, 0, -1):
    print(f"{i}", end = "")
    print(" x " if i > 1 else " = ", end = "")
    factorial *= i
print(f"{factorial}")
