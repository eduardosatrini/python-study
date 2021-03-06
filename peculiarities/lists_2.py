fruits = list()
fruit = list()

for i in range(0, 3):
    fruit.append(str(input("Fruit:").strip()))
    fruit.append(str(input("Color:").strip()))
    fruits.append(fruit[:])
    fruit.clear()
print(fruits)
