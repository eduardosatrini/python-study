from calcs import calcs

v = float(input("Type a value: R$"))
print(f"Half: R${calcs.half(v):.2f}")
print(f"Double: R${calcs.double(v):.2f}")
print(f"Increase 22%: R${calcs.increase_percent(v, 22)}")
