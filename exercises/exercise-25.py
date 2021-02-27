distance = float(input("Travelled distance: "))
price = distance * 0.50 if distance <= 200 else distance * 0.45
print("Trip price: R${:.2f}".format(price))

