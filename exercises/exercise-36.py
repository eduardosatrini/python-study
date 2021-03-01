seg_1 = int(input("First segment: "))
seg_2 = int(input("Second segment: "))
seg_3 = int(input("Third segment: "))

if seg_1 < (seg_2 + seg_3) and seg_2 < (seg_1 + seg_3) and seg_3 < (seg_1 + seg_2):
    triangle_form = ""
    if seg_1 == seg_2 == seg_3:
        triangle_form = "equilateral."
    elif seg_1 != seg_2 != seg_3 != seg_1:
        triangle_form = "scalene."
    else:
        triangle_form = "isosceles."          
    print(f"Can form a triangle {triangle_form}") 
else:
    print("Cannot form a triangle!")
