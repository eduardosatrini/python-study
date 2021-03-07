# Calc major, minor and equals numbers

n1 = int(input("First number: "))
n2 = int(input("Second number: "))

if n1 > n2:
	print("First is major!")
elif n2 > n1:
	print(f"Second is major")
else:
	print("Numbers equals!")
