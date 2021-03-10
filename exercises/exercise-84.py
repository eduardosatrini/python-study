# More about matriz

matriz = [[], [], []]
sum_even = 0
sum_values_3_column = 0
major_value_second_line = 0

for line in range(0, 3):
    for column in range(0, 3):
        num = int(input(f"Enter a number [{line}, {column}]: "))
        matriz[line].append(num) 
        
for line in range(0, 3):
    for column in range(0, 3):
        print(f"[{matriz[line][column]}] ", end = "")

        if matriz[line][column] % 2 == 0:
            sum_even += matriz[line][column]
            
        if matriz[1][column] > major_value_second_line:
            major_value_second_line = matriz[1][column]
            
    sum_values_3_column += matriz[line][2]
    print()
    
print("=-"*12)
print(f"Sum all even is: {sum_even}")
print(f"Sum all values in third column is: {sum_values_3_column}")
print(f"Major value the second line is: {major_value_second_line}") 
