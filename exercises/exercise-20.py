name = str(input("Your complete name: ")).strip().lower()

f_name = name.find("a") + 1
r_name = name.rfind("a") + 1
print("The letter A appears:", name.count("a"), "times")
print("The first letter A appears:", f_name, "position")
print("The last letter A appears:", r_name)