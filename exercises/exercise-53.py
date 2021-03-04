from random import randint

computer = randint(1, 10)
tried = 0
chances = 3
while True:
    number = int(input(f"Wich number I think (chances {chances}): "))
    if number == computer:
        print(f"Tried: {tried}")
        print(f"You win! I think in {computer}")
        break
    elif number < computer:
        if chances == 0:
            print(f"You loose! I think in {computer}")
            break
        print("Wrong! more..")
    elif number > computer:
        if chances == 0:
            print(f"You loose! I think in {computer}")
            break
        print("Wrong! less..")
    tried += 1
    chances -= 1
