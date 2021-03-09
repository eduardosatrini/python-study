from colore import colore as c

numbers = []
even = []
odd = []
while True:
    num = int(input(c(":b:Enter a number::b_:")))
    numbers.append(num)

    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

    keep = str(input(c("Continue? :b:[Y/N]::b_: "))).strip().upper()

    if keep != "Y":
        break
print(c(f"Total: :green:{numbers}:green_:"))
print(c(f"Even numbers of list: :green:{even}:green_:"))
print(c(f"Odd numbers of list: :green:{odd}:green_:"))
print("Program end..")
