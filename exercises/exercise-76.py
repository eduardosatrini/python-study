# Sorted and set numbers

numbers = []
while True:
    num  = int(input("Enter a value: "))
    numbers.append(num)

    keep = str(input("Continue? [Y/N]: ")).strip().upper()
    if keep != "Y":
        break
print("=-"*20)
print(f"Values: {sorted(set(numbers))}")        

    
