seg_1 = float(input("First segment: "))
seg_2 = float(input("Second segment: "))
seg_3 = float(input("Third segment: "))

if seg_1 < (seg_2 + seg_3) and seg_2 < (seg_1 + seg_3) and seg_3 < (seg_1 + seg_2):
	print("Triangle!")
else:
	print("Not Triangle!")


