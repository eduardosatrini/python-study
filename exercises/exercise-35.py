# Calc 

from datetime import date

birth = int(input("Year of birth:"))
year = date.today().year
years_old = year - birth

if years_old <= 12:
	print("Mirin!")
elif years_old > 12 and years_old <= 18:
	print("Junior!")
elif years_old > 18 and years_old <= 22:
	print("Senior!")
elif years_old > 22:
	print("Master!")

