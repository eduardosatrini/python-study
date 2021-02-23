days = int(input("Rented days: "))
traveled = float(input("Km travaled: "))
value_pay = days * 60
value_km  = traveled * 0.15
total = value_pay + value_km
print("Totally to pay: ${:.2f}".format(total))