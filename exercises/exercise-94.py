from time import sleep

def my_count(start, close, jump = 1):

    print(f"Counting from {start} to {close} jumping from {jump} to {jump}.")

    if jump < 0:
        jump *= -1

    if start < close:
        i = start
        while i <= close:
            print(f"{i}", end = " ", flush = True)
            sleep(0.3 )
            i += jump
        print("END.")
    else:
        i = start
        while i >= close:
            print(f"{i}", end = " ", flush = True)
            sleep(0.3)
            i -= jump
        print("END.")
        

my_count(5, 50, 5)
print("=-"*20)

my_count(50, 5, 5)
print("=-"*20)

print("It's your time!")
s = int(input("Start: "))
c = int(input("Close: "))
j = int(input("Jump: "))
my_count(s, c, j)
print("=-"*20)
