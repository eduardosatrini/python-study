from random import randint

prices_1 = []
for p in range(6): # example without list comprehension
    prices_1.append(float(randint(1, 99)))
print(f"{prices_1}")

# same example with list comprehension
prices_2 = [float(randint(1, 99)) for p in range(6)]
print(f"{prices_2}")
