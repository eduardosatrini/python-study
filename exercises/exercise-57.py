first = int(input("First term: "))
reason = int(input("Reason: "))
term = first

c = 1
total = 0
more = 10
while more != 0:
    total += more
    while c <= total:
        print(f"{term} -> ", end = "")
        term += reason
        c += 1
    print("PAUSE")
    more = int(input("How many terms do you want to show? "))
print(f"Total terms: {total} | End program..")


