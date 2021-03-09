# Sorted a list with dynamic
numbers = []
for i in range(0, 5):
    num = int(input("Enter a value: "))

    if i == 0 or num > numbers[-1]:
        numbers.append(num)
    else:
        position = 0
        while position < len(numbers):
            if num <= numbers[position]:
                numbers.insert(position, num)
                break
            position +=1
print("-="*20)
print(numbers)
            
