sum_age = 0
older_age = 0
older_name = ""
total_woman = 0
for i in range(1, 5):
    print(f"======= {i}º Person =======")
    name = str(input("Name: ")).strip()
    age = int(input("Age: "))
    sex = str(input("Sex [m/f]: ")).strip().lower()

    if i == 1:
        older_name = name
        older_age = age
    else:
        if age > older_age and sex == "m":
            older_age = age
            older_name = name
    if sex == "f" and age < 20:
        total_woman += 1
        
    sum_age += age    
media = sum_age / 4

print(f"More older name: {older_name} | older age: {older_age}")
print(f"Media age: {media:.1f}")
print(f"Total woman under 20: {total_woman}") 
