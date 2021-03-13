# program interactive help python
from colore import colore as c

def command_help(command):
    print(f"Manual {command}")
    help(command)


def view(msg):
    size = len(msg)
    print(c(":b:=-:b_:") * size)
    print(c(f":blue:{msg}:blue_:"))
    print(c(":b:=-:b_:") * size)

    
command = ""
while True:
    view("PyHELP")
    command = str(input("Function or Library > ")).strip().lower()
    if command.upper() == "END":
        break
    else:
        command_help(command)
