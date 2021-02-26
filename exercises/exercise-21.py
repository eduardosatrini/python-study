full_name = str(input("Your complete name: ")).strip()

split_name = full_name.split()
first_name = split_name[0]
last_name = split_name[-1]

print(f"First name: {first_name}")
print(f"Last name: {last_name}")