# Major in minor numbers the list
numbers = [] 
for i in range(0, 5):
    num = int(input(f"Enter a value in position {i}º: ")) 
    numbers.append(num)
    
print(f"Values: {numbers}")
print(f"=-"*18)

print(f"Major: {max(numbers)} | Position: ", end = "")    
for key, value in enumerate(numbers):
    if value == max(numbers):
        print(f" {key}º ", end = "")
print()        
print(f"Minor: {min(numbers)} | Position: ", end = "")
for key, value in enumerate(numbers):
    if value == min(numbers):
        print(f" {key}º ", end = "")

