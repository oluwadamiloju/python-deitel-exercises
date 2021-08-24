def first_triangle():
    for line in range(1, 11):
        for stars in range(1, line):
            print('*', end="")
        print("")


print(first_triangle())


def second_triangle():
    for line in range(1, 11):
        for stars in range(10, line, -1):
            print('*', end="")
        print()


print(second_triangle())


def third_triangle():
    for line in range(1, 11):
        for spaces in range(1, line):
            print(" ", end="")
        for stars in range(10, line, -1):
            print("*", end="")

        print()


print(third_triangle())


def fourth_triangle():
    for line in range(1, 11):
        for spaces in range(9, line - 1, -1):
            print(" ", end="")
        for stars in range(1, line):
            print("*", end="")
        print()


print(fourth_triangle())
