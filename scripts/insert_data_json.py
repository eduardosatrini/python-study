import json

def insert(data):
	with open('dados.json', 'w') as f:
		f.write(json.dumps(data))

insert(["Eduardo", "Maria", "John"])
