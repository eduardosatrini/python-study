from datetime import datetime

employee = dict()
employee["name"] = str(input("Name: ")).strip()
birth = int(input("Birth date: "))
employee["years_old"] =  datetime.now().year - birth
employee["work_card"] = int(input("Work card: (0 for nothing)"))

if employee["work_card"] != 0:
    employee["year_hiring"] = int(input("Year of hiring? "))
    employee["salary"] = float(input("Salary: R$"))
    employee["retirement"] = employee["years_old"] + ((employee["year_hiring"] + 35) - datetime.now().year)
print("=-"*12)
for key, value in employee.items():
    print(f"{key} - {value}")
 
