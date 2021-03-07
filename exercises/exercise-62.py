from time import sleep
while True:
    num = int(input("Value [0 for quit]: "))
    if num == 0:
        break
    print("=-"*12)
    for i in range(1, 11):
        print(f"{num} x {i} = {num*i}")
    print("=-"*12)
sleep(0.5)
print("End program..")        
