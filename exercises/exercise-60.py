num = int(input("Type a number: "))
res = input("Continue? [Y/N]: ").strip().lower()

c = 1
total = major = minor = num
while res != "n":
    num = int(input("Type a number: ")) 
    res = input("Continue? [Y/N]: ").strip().lower()
    if num > major:
        major = num
    elif num < minor:
        minor = num
    total += num
    c += 1
media = total / c

print("=-"*12)
print(f"Typed: {c} | Media: {media:.1f}")
print(f"Major: {major} | Minor: {minor}")
print("End program..")        
    
