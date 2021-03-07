while True:
    print("""
============================
Choose one bases for convert:
[1] Convert binary
[2] Convert Octal
[3] Convert Hexadecimal
    """)
    num = int(input("Enter a number: "))
    option = int(input("Your option: "))

    if option < 1 or option > 3:
        print("Invalid value.")
        break
    else:
        if option == 1:
            print(f"Binary: {bin(num)[2:]}")
        elif option == 2:
            print(f"Octal: {oct(num)[2:]}")
        else:
            print(f"Hexadecimal: {hex(num)[2:]}")
    
        keep = str(input("Continue [Y/N]: ")).strip().upper()
        if keep != "Y":
            break
print("End program..")
