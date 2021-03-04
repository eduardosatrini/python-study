while True:
    genrer = str(input("Your genrer: ")).strip().lower()
    if genrer == "m" or genrer == "f":
        print("Registered with success!")
        print(f"Genrer: {genrer}")
        break
    print("invalid input!")
print("End program..")
