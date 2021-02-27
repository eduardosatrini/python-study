from datetime import date
year = int(input("Choose a year (0 for actual year):"))

if year == 0:
    year = date.today().year

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f"{year} - Leap year: YES!")
else:
    print(f"{year} - Leap year: NO!")

