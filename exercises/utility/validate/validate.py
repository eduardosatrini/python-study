def coin(msg):
    valid = False
    while not valid:
        enter = str(input(msg)).strip().lower()

        if enter.isalpha() or enter == "":
            print("Error - price invalid. ")
        else:
            valid = True
            return float(enter)
