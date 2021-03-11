# Register futball player
player = dict()
goals = list()
sum_goals = 0
player["name"] = str(input("Futball player name: ")).strip()
player["match"] = int(input(f"How many games did {player['name']} play: "))

for i in range(0, player["match"]):
    goals.append(int(input(f"How many goals in the match {i+1}º? ")))

player["goals"] = goals

print("=-"*20)
for k, v in player.items():
    print(f"{k} - {v}")

print("=-"*20)
print(f"The player {player['name']} played {player['match']} matchs.")

for k, v in enumerate(goals):
    print(f"    ==> In the match {k+1} did {v} goals.")
    sum_goals += v

print(f"Total goals: {sum_goals}")
print("=-"*20)

print(player)
