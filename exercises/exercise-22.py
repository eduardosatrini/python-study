# Thinking in random number

from random import randint
from time import sleep

num = int(input("What number to think from 1 to 5? "))
rand_num = randint(1, 5)

print("Thinking..")
sleep(1)

if num == rand_num:
    print(f"You win!, I think {rand_num}.")
else:
    print(f"I Win!, I think {rand_num}.")