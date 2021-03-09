# Valid a simples expression with "(" ")"

from colore import colore as cor

expression = str(input("Enter a expression: ")).strip()

l = []

for simb in expression:
    if simb == "(":
        l.append("(")
    elif simb == ")":
        if len(l) > 0:
            l.pop()
        else:
            l.append(")")
            break
if len(l) == 0:
    print(cor(":green:Correct expression!:green_:"))
else:
    print(cor(":red:Wrong expression!:red_:"))
