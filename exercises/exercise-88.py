# Ranking with game die
from random import randint
from time import sleep
from operator import itemgetter

players = {
    'player_1': randint(1, 6),
    'player_2': randint(1, 6),
    'player_3': randint(1, 6),
    'player_4': randint(1, 6)}
    
ranking = dict()

for key, value in players.items():
    print(f"{key}: {value}")
    sleep(0.5)
    
print("=-"*12)
print(f"RANKING")

ranking = sorted(players.items(), key = itemgetter(1), reverse = True)
for key, value in enumerate(ranking):
    print(f"{key+1} - {value[0]} - {value[1]}")
    sleep(0.5)


