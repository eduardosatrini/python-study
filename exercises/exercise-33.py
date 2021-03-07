# Calc ficcional date enlistment 

from datetime import date

birth = int(input("Birth date: "))
year = date.today().year
years_old = year - birth

print(f"Who's born in {birth} have {years_old} years old in {year}.")
if years_old == 18:
	print("Enlistment year!")
elif years_old < 18:
	remaining = 18 - years_old
	v1 = year + remaining
	print(f"You have {remaining} years ({v1}) to present yourself in the army!")
elif years_old > 18:
	s_year = years_old - 18
	v2 = year - s_year
	print(f"{s_year} years ({v2}) ago you should have enlisted in the army!")
