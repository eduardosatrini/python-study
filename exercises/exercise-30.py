# Calc rent

house_price = float(input("House price: R$"))
salary    = float(input("Your salary: R$"))
years_pay = int(input("Years to pay: "))

prestation = house_price / (years_pay * 12)
salary_min = (salary * 30 / 100)

print("Prestation: R${:.2f}".format(prestation))
print("30% salary: R${:.2f}".format(salary_min))
if prestation <= salary_min:
	print("Status: Loan accept!")
else:
	print("Status: Loan refused!")

