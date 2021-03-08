# Sort numbers in tuple
from random import randint

nums = (randint(1, 10), randint(1, 10), randint(1, 10), 
        randint(1, 10), randint(1, 10), randint(1, 10))
        
for i in nums:
    print(f"{i} ", end = "") 
print(f"\nMajor: {max(nums)} | Minor: {min(nums)}")
