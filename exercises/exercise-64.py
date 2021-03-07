print("Register users")
print("=-"*12)

total_more_18 = total_men = total_woman_more_20 = 0
while True:

    name = str(input("Name: ")).strip()
    age = int(input("Age: "))
    genrer = str(input("Genrer [M/F]: ")).strip().upper()

    if genrer != "M" and genrer != "F": 
        print("Genrer invalid!")
        break

    if age >= 18:
        total_more_18 += 1
    if genrer == "M":
        total_men += 1
    if genrer == "M" and age <= 20:
        total_woman_more_20 += 1
        
    print("="*12)
    keep = str(input("Continue [Y/N]?")).strip().upper()

    if keep != "Y":
        break
print(f"Total users who are over 18: {total_more_18}")
print(f"Total registered men: {total_men}")
print(f"Total woman under 20 years of age: {total_woman_more_20}")
print("End program..")
