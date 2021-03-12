from random import sample, randint
from time import sleep

def major_number(*num):
    print("Analysing..")
    for n in num:
        print(n, end = " ", flush = True)
        sleep(0.5)
    print()   
    print(f"Total: {len(num)} - Major number: {max(num)}")

major_number(
    2, 4, 234, 5345, 23424, 765, 234
)
print("=-"*20)

major_number(
    432, 35, 454, 11, 76, 889,
)
print("=-"*20)

major_number(
    3, 5, 123, 7, 1223, 76, 235, 1234
)
print("=-"*20)
