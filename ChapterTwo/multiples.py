first_number = int(input("Enter a number: "))
second_number = int(input("Enter a number: "))

if first_number % second_number == 0:
    print("the second number is a multiple of the first number")


if second_number % first_number == 0:
    print("the first number is a multiple of the second number")
