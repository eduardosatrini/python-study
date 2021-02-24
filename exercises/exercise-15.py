import random

name1 = input("Name 1°: ")
name2 = input("Name 2°: ")
name3 = input("Name 3°: ")

names = [name1, name2, name3]
print("Old order:", names)

random.shuffle(names)
print("New order:", names)
