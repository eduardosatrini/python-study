# Analyse a list
numbers = []
even = []
for i in range(0, 4):
    number = int(input("Enter a number: "))
     
    if number % 2 == 0:
        even.append(number)
        
    numbers.append(number)    
print(f"Values: {numbers}")
print(f"Value 9 appeared: {numbers.count(9)} times")
if 3 in numbers: # gambi(?)
    print(f"Number 3 appeared in position: {numbers.index(3)+1}")
print(f"Even numbers: {even}")
