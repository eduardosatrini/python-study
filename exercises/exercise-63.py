from random import randint
total_win = 0
while True:
    player_value = int(input("Value: "))
    player_option = str(input("Even or Odd [E/O]:")).strip().lower()

    if player_option != "e" and player_option != "o":
        print("Input invalid!")
        break
    
    computer_value = randint(1, 10)
    total = player_value + computer_value
    print(f"You: {player_value} - Computer: {computer_value}")
    print(f"Total: {total} - ", end = "")
    print("EVEN!" if total % 2 == 0 else "ODD!")
    
    if player_option == "e":
        if total % 2 == 0:
            print("You win!")
            total_win += 1
        else:
            print("You lose!")
            break         
    elif player_option == "o":
        if total % 2 == 1:
            print("You win!")
            total_win += 1
        else:
            print("You lose!")
            break
print(f"Total win: {total_win}")
print("End game..")
