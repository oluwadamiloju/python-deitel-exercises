sample_string = input("Enter a string")

vowel = ['a', 'e', 'i', 'o', 'u']
is_contained = False
for char in sample_string:
    for letter in vowel:
        if letter == char:
            is_contained = True
            break

if is_contained:
    print("String contains a vowel")
else:
    print("String does not contain a vowel")
