n1 = int(input("First number: "))
n2 = int(input("Second number: "))

while True:
    print("""
    [1] Sum
    [2] Multiply
    [3] Major
    [4] New numbers
    [5] Quit
    """)
    option = int(input(">>> What's your option: "))
    print("=-"*12)
    if option == 1:
        s = n1 + n2
        print(f">>>>> Sum: {s}")
    elif option == 2:
        m = n1 * n2
        print(f">>>>> Multiply: {m}")
    elif option == 3:
        if n1 > n2:
            major = n1
        else:
            major = n2
        print(f">>>>> Major: {major}")
    elif option == 4:
        n1 = int(input(">>> First number: "))
        n2 = int(input(">>> Second number: "))
    elif option == 5:
        print(">>>>> End program..")
        break
    print("=-"*12)

    
