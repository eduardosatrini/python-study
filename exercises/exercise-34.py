# Calc student's media

n1 = float(input("Student grade 1: "))
n2 = float(input("Student grade 2: "))

m = (n1 + n2) / 2
if m < 5.0:
	print(f"Media: {m}")
	print("Failed  student!")
elif 6 >= m >= 5:
	print(f"Media: {m}")
	print("Recovery student!")
else:
	print(f"Media: {m}")
	print("Approved student")
