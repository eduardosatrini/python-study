print("===== Calc AP =====")

first = int(input("First term: "))
reason = int(input("Reason: "))
term = first
c = 1

while c <= 10:
    print(f"{term} -> ", end = "")
    term += reason     
    c += 1
