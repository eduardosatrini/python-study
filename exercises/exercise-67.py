# Fibonnaci v2 

def fib(num):
    a, b = 0, 1
    while a < num:
        print(a, end = " ")
        a, b = b, a+b
    print()
num = int(input("Value: "))
fib(num) 
