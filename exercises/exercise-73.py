# Show fruits and price with tuple

fruits = (
    ("Apple", 5.75), ("Orange", 3.0), ("Meloon", 8), 
    ("Watermeloon", 12), ("Grape", 17), ("Tomato", 2)
)

print("{:^25}".format("MARKET"))
print("=-"*13)
for fruit in fruits:
    print(f"{fruit[0]:.<18} R${fruit[1]:.2f}")
