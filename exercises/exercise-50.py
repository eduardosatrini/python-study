# Weight min and max in KG

weight_max = 0
weight_min = 0
for i in range(1, 6):
    weight = float(input(f"Weight of {i}º person: (KG)"))
    if i == 1:
        weight_max = weight
        weight_min = weight
    else:
        if weight > weight_max:
            weight_max = weight
        if weight < weight_min:
            weight_min = weight
print(f"Max weight: {weight_max:.1f}")
print(f"Min weight: {weight_min:.1f}")
print("End program..")
