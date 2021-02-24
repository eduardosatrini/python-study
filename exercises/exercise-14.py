from random import choice

name1 = input("Name 1°: ")
name2 = input("Name 2°: ")
name3 = input("Name 3°: ")

names = [name1, name2, name3]

chosen = choice(names)
print("Chosen student:", chosen)
