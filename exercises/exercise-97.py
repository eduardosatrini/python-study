from datetime import datetime

def status_vote(year):
    years_old = datetime.today().year - year
    if years_old < 16:
        return f"With {years_old}, Don't vote!"
    elif years_old >= 16 and years_old < 18:
        return f"With {years_old}, Vote is optional!"
    else:
        return f"With {years_old}, Vote is mandatory!"

year = int(input("What year were you born? "))
print(status_vote(year))

