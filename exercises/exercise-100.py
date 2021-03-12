def confirm_numeric():
    while True:
        n = str(input("Enter a positive number: ")).strip()
        if n.isnumeric():
            print(f"{n} correct input!")
            break
        print(f"{n} Is not a positive number.")
        

confirm_numeric()
