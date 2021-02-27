salary = float(input("Salary: R$"))

if salary <= 1250:
    readjustment = salary + (salary * 15 / 100)
    print("Ajust salary : (+15%) R${:.2f}".format(readjustment))
else:
    readjustment = salary + (salary * 10 / 100)
    print("Ajust salary : (+10%) R${:.2f}".format(readjustment))



