# program for calc rented and km traveled

days = int(input("Rented days: "))
traveled = float(input("Km traveled: "))
value_pay = days * 60
value_km  = traveled * 0.15
total = value_pay + value_km
print("Totally to pay: ${:.2f}".format(total))