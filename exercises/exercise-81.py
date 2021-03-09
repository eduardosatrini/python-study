# Show a list with name and weight  
from colore import colore as c

user = []
users = []
minor = major = 0
while True:
    name = str(input(c(":blue:Name: :blue_:"))).strip()
    weight = float(input(c(":blue:Weight: :blue_:")))  

    if len(users) == 0:
        minor = major = weight

    if weight > major:
        major = weight
    if weight < minor:
        minor = weight
    
    user.append(name)
    user.append(weight)
    users.append(user[:])
    user.clear()

    keep = str(input(c("Continue: :b:[Y/N]:b_: "))).strip().upper()

    if keep != "Y":
        break
print(c(f"Total users registered: :green:{len(users)}:green_:"))

print(f"Major weights: {major} ", end = "")
for user in users:
    if user[1] == major:
        print(f"({user[0]})", end = " ")
        
print()

print(f"Minor weights: {minor} ", end = "")
for user in users:
    if user[1] == minor:
        print(f"({user[0]})", end = " ")


