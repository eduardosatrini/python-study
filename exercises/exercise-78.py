from colore import colore as c

numbers = []
while True:
    num = int(input("Enter a number: "))
    numbers.append(num)

    keep = str(input(c(":b:Continue? [Y/N]: :b_:"))).strip().upper()

    if keep != "Y":
        break
print(c(f"Total values: :green:{len(numbers)}:green_:"))
print(c(f"Decreasing order: :green:{sorted(numbers)[::-1]}:green_:"))
if 5 in numbers:
    print(c("Value :green:5:green_: exists in list."))
else:
    print(c("Value :green:5:green_: not exists in list."))
print("End program..")
            
    
