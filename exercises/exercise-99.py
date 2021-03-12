def total_goals(name = "<unknown>", goals = 0):
    print(f"Name player: {name}")
    print(f"Total goals: {goals}")
    print("=-"*20)


name = str(input("Name: "))
g = str(input("Goals: "))

if g.isnumeric():
    g = int(g)
else:
    g = 0

if name.strip() == "":
    total_goals(goals = g)
else:
    total_goals(name, g)
