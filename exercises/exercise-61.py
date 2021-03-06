total = c = 0
while True:
    num = int(input("Type a number (999 for stop):"))
    if num == 999:
        break
    c += 1
    total += num
print(f"Total numbers: {c}")    
print(f"Sum all numbers is: {total}")
