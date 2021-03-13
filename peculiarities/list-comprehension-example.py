fruits = ["Banana", "Apple", "Watermelon"]

for fruit in fruits: # without list comprehension
    if "n" in fruit:
        print(fruit, end = " ")
print()

# with list comprehension
fruit2 = [fruit for fruit in fruits if "n" in fruit]
print(fruit2)
