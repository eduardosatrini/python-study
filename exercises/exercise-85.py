# Sort mega sena
from random import sample
from time import sleep

num = int(input("How many numbers will be drawn? "))

for i in range(0, num):
    print(f"Game {i+1}º {sorted(sample(range(1, 61), 6))}")
    sleep(0.5)
