# Total majors and minors

from datetime import date

total_major = 0
total_minor = 0

for i in range(0, 7):
    year = int(input(f"What year was the {i+1}º person born? "))
    if (date.today().year - year) < 18:
        total_minor += 1
    else:
        total_major += 1
print(f"Total major: {total_major}")
print(f"Total minor: {total_minor}")
print("Program end..")
