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