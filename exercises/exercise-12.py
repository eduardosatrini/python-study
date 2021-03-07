# Calc Hipotenuse
from math import hypot

opposite = float(input("Opposite leg length: "))
adjacent = float(input("Adjacent leg length: "))

# hipotenuse = (opposite ** 2 + adjacent ** 2) ** (1/2)
# print("The hypotenuse measure: {:.3f}".format(hipotenuse))

print("The hypotenuse measure: {:.3f}".format(hypot(opposite, adjacent)))
