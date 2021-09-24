# 2.9 (Integer Value of a Character) Here’s a peek ahead. In this chapter, you learned
# about strings. Each of a string’s characters has an integer representation.
# The set of characters a computer uses together with the characters’ integer representations is called
# that  computer’s character set. You can indicate a character value in a program by enclosing that
# character in quotes, as in 'A'. To determine a character’s integer value, call the built-in
# function ord:

    # In [1]: ord('A')
    # Out[1]: 65

# Display the integer equivalents of B C D b c d 0 1 2 $ * + and the space character.

print("The integer value of B is", ord('B'))
print("The integer value of C is", ord('C'))
print("The integer value of D is", ord('D'))
print("The integer value of b is", ord('b'))
print("The integer value of c is", ord('c'))
print("The integer value of d is", ord('d'))
print("The integer value of 0 is", ord('0'))
print("The integer value of 1 is", ord('1'))
print("The integer value of 2 is", ord('2'))
print("The integer value of $ is", ord('$'))
print("The integer value of * is", ord('*'))
print("The integer value of + is", ord('+'))
print("The integer value of space is", ord(' '))