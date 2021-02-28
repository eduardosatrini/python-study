import re

for i in range(32, 10_000):
	ch = chr(i)
	if re.match('\d', ch):
		print(ch, end = "")
print("")
