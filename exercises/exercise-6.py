# Calc area width and height

w = float(input("Width: "))
h = float(input("Height: "))

area  = w * h
paint = area / 2
print("Dimension: {}x{} and Area: {}m²".format(w, h, area))
print("liter of paint needed to clean the wall: {}".format(paint))

