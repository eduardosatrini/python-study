import math
n = float(input("Type an angle:"))
n = math.radians(n)

seno = math.sin(n)
cos = math.cos(n)
tan = math.tan(n)

print("Sen: {:.2f}".format(seno))
print("Cos: {:.2f}".format(cos))
print("Tan: {:.2f}".format(tan))