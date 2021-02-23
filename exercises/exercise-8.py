value = float(input("Your salary: :) $"))
increase = value * 15 / 100
salary = increase + value

print("Your actual salary with 15% ({:.2f}) increase is: ${:.2f}".format(increase, salary))