txt = input("Type a pharse: ")

print("Size: ", len(txt))
print("number of letters 'a':", txt.count('a'))
print("Find:", txt.find('en'))
print("E In:", 'E' in txt)
print("Replace:", txt.replace('a', 'e'))

print(txt.upper())
print(txt.lower())
print(txt.capitalize())
print(txt.title())
print("No spaces:", txt.strip())

print("Strip: ", txt.split(), "Join:", "#".join(txt))