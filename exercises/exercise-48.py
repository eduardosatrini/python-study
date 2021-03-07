# Palindrome

txt = str(input("Type: ")).strip().lower()

txt_split = txt.split()
txt_join = "".join(txt_split)    
txt_inverse = ""

for i in range(len(txt_join)-1, -1, -1):
    txt_inverse += txt_join[i]
print("Reverse: {}".format(txt_inverse.capitalize()))

if txt_join == txt_inverse:
    print("Palindrome!")
else:
    print("Not palindrome!")
