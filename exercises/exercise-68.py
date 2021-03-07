# Shows numbers in full from 0 to 20

numbers = ("Zero", "One", "Two", "Three", "Four", "Five", 
        "Six", "Seven", "Eight", "Nine", "Ten",
        "Eleven", "Twelve", "Thirtteen", "Fourteen", "Fifteen", 
        "Sixteen", "Seventeen", "Eighteen", "Nineteen", "Twenty")
while True: 
    num = int(input("Enter a number between 0 and 20: "))
    if 0 <= num <= 20: 
        print(f"Full: {numbers[num]}")
        keep = str(input("Continue [Y/N]: ")).strip().upper()
        if keep != "Y":
            break
    else:
        print("Try again.", end = " ")
        
print("End program..")
