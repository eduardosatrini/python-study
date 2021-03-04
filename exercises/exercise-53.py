from random import randint

computer = randint(1, 10)
tried = 0
while True:
    number = int(input("Wich number I think: "))
    if number == computer:
        print(f"Tried: {tried}")
        print(f"You win! I think in {computer}")
        break
    elif number < computer:
        print("Wrong! more..")
    elif number > computer:
        print("Wrong! more..")
    tried += 1
