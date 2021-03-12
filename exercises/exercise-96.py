from random import randint

def drawing_values(amount):
    return sample(range(1, 9), amount) 


def sum_even(values):
    s = 0
    for i in values:
        if i % 2 == 0:
            s += i
    return s


v = drawing_values(5)    
print(f"{len(v)} values in the list: {v}")
print(f"Sum evens: {sum_even(v)}")
