# Using dictionaries
from colore import colore as c
student = {}
student["name"] = str(input("Student name:")).strip()
student["media"] = float(input("Media: "))

print(f"Name: {student['name']}")
print(f"Media: {student['media']}")

if student["media"] <= 5:
    print(c(f"Status: :red:Reproved:red_:"))
elif 5 < student["media"] <= 6:
    print(f"Status: Recovery")
else:
    print(c(f"Status: :blue:Aproved:blue_:"))
