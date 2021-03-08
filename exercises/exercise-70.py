print("CBLOL TEAMS")

cblol_teams = (
    "Flamengo", "Red Canids", "Pain", "Rensga", "Furia",
    "Cruzeiro", "INTZ", "Loud", "Kabum", "Vorax"
)

for k, v in enumerate(cblol_teams):
    if k <= 3:
        print("\033[32m", f"{k+1}º - {v}", "\033[0:0m")
    elif k >= 8:
        print("\033[31m", f"{k+1}º - {v}", "\033[0:0m")
    else:
        print(f" {k+1}º - {v}")

cblol_teams_sorted = sorted(cblol_teams)

print("Sorted")
for k, v in enumerate(cblol_teams_sorted):
    print(f"{k}º - {v}")
