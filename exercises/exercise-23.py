# Calc velocity the driver

velo = int(input("Current car speed: "))

if velo <= 80:
    print("All very well! have a good trip!")
else:
    traffic_ticket = (velo - 80) * 7
    print("Above the allowed!")
    print(f"traffic ticket: {traffic_ticket}")