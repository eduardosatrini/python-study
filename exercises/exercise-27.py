# Calc major and minor number

n1 = int(input("1º number: "))
n2 = int(input("2º number: "))
n3 = int(input("3º number: "))

major = n1
if n2 > n1 and n2 > n3:
    major = n2
if n3 > n1 and n3 > n2:
    major = n3

minor = n1
if n2 < n1 and n2 < n3:
    minor = n2
if n3 < n1 and n3 < n2:
    minor = n3

print(f"Major: {major}")
print(f"Minor: {minor}")
