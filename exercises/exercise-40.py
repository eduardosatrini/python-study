from random import randint 

print("""
Options:
[0] Rock
[1] Paper
[2] Scissors
""")

chooses = ('Rock', 'Paper', 'Scissors')
computer = randint(0, 2)
player = int(input("Your move: "))

print("Computer play: {}".format(chooses[computer]))
print("Your play: {}".format(chooses[player]))

win = ""
if computer == 0: # ROCK
    if player == 0:
        win = "TIE!"
    elif player == 1:
        win = "YOU!"
    elif player == 2:
        win = "COMPUTER!"
    else:
        win = "INVALID!"
elif computer == 1: # PAPER
    if player == 1:
        win = "TIE!"
    elif player == 0:
        win = "COMPUTER!"
    elif player == 2:
        win = "YOU!"
    else:
        win = "INVALID!"
elif computer == 2: # SCISSORS
    if player == 2:
        win = "TIE!"
    elif player == 0:
        win = "YOU!"
    elif player == 1:
        win = "COMPUTER!"
    else:
        win = "INVALID!"

print(f"Winner: {win}")
