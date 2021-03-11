# Calc area perimeter

def area(width, height):
    area =  width * height
    print(f"Area: {width:.1f}x{height:.1f} is {area:.1f}m².")
    

print("Land control")
print("=-"*20)
width = float(input("Width: "))
height = float(input("Height: "))
area(width, height)

    
