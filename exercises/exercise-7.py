# Calc discount

value = float(input("Price of the product: $"))
discount = value * 5 / 100
prod = value - discount

print("${:.2f} with 5%(${:.2f}) new value: ${:.2f}".format(value, discount, prod))