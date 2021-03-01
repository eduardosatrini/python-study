weigh = float(input("How much do you weigh? KG"))
height = float(input("How tall are you? (M)"))
# normal, obesity morbid, under normal weight, over weigh
bmi = weigh / (height ** 2)

if bmi < 18.5:
    print(f"Your BMI is {bmi}")
    print("You are in the {} weight range!")
elif bmi >= 18.5 and bmi < 25:
    print(f"Your BMI is {bmi}")
    print("You are in the normal weight range!")
elif bmi >= 25 and bmi < 30:
    print(f"Your BMI is {bmi}")
    print("You are in the under normal weight range!")
elif bmi >= 30 and bmi < 40:
    print(f"Your BMI is {bmi}")
    print("You are in the obesity weight range!") 
else:
    print(f"Your BMI is {bmi}")
    print("You are in the obesity morbid weight range!")
