# Unify dictionaries and lists
user = dict()
users = list()
total_age = 0
while True:
    user["name"] = str(input("Name: ")).strip()
    while True:
        user["genrer"] = str(input("Genrer [M/F]: ")).strip().upper()
        if user["genrer"] in "MF":
            break
        print("Please! just M or F. ", end = "")
        
    user["age"] = int(input("Age: "))
    total_age += user["age"]
    users.append(user.copy())
    user.clear()
    
    while True:
        keep = str(input("Continue [Y/N]: ")).strip().upper()
        if keep in "YN":
            break
        print("Please! just Y or N.", end = "")
    if keep == "N":
        break
print("=-"*20)
print(f"Total register users: {len(users)}")

total_woman = list() 
for u in users:
    if u["genrer"] == "F":
        total_woman.append(u["name"])      
media = total_age / len(users)

print(f"Media: {media:.1f}")
print(f"Total woman registered: {total_woman}")

print("Above average age:")
for m in users:
    if m["age"] > media:
        print(f"===> {m['name']} -  {m['age']}")
print("Program end..")
