# 3.18 (Challenge: Nested Looping) Modify your script from Exercise 3.17 to display all
# four patterns side-by-side (as shown above) by making clever use of nested for loops.
# Separate each triangle from the next by three horizontal spaces. [Hint: One for loop should
# control the row number. Its nested for loops should calculate from the row number the
# appropriate number of asterisks and spaces for each of the four patterns.]

for rows in range(1, 11):
    for stars in range(1, rows):
        print('*', end="")
    for spaces in range(14, rows, -1):
        print(' ', end="")
    for stars in range(10, rows, -1):
        print('*', end="")
    for spaces in range(0, rows):
        print('  ', end="")
    for stars in range(10, rows, -1):
        print('*', end="")
    for spaces in range(14, rows, -1):
        print(' ', end="")
    for stars in range(1, rows):
        print('*', end="")
    print()
