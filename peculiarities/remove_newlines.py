# remove newline scape characters from the strings in a list

colors = ["Red\n", "Green\n", "Blue\n"]
print(colors)

colors = [
    color.strip() for color in colors
    # list comprehension
]
print(colors)

