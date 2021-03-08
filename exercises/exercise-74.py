# Verify vowel in word

languages = (
    "Python", "Ruby", "Javascript", "Rust",
    "Go", "Dart", "C#", "C++", "Java", "PHP"
)

for lang in languages:
    print(f"In word {lang} have: ", end = "")
    for letter in lang:
        if letter in "aeiouAEIOU":
            print(letter.upper(), end = " ")
    print()
            
            
