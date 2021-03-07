# Prime number

num = int(input("Type a number: "))
total = 0 
for i in range(1, num+1):
    if num % i == 0:
        total += 1
print(f"Total div: {total}")
if total == 2:
    print("IS PRIME!")
else:
    print("NOT PRIME!")
