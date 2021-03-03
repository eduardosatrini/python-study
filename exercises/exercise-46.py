first_term = int(input("First term: "))
reason = int(input("Reason: "))
ten_term = first_term + (10 - 1) * reason
for i in range(first_term, ten_term, reason):
    print(f"{i}", end = " -> ")
print("END..")
