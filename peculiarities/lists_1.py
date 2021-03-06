# LISTS

animals = []
 
cat = []
cat.append("Niko")
cat.append(2)
animals.append(cat)

dog = []
dog.append("Bobby")
dog.append(4)
animals.append(dog)

for animal in animals:
    print(f"name: {animal[0]} | age: {animal[1]}")
