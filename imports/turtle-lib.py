from turtle import pencolor, forward, right
from random import choice, randint

cho_1 = ('blue', 'green', 'red')
for x in range(500):
	pencolor(choice(cho_1))
	forward(randint(1, 50))
	right(randint(33, 90))
