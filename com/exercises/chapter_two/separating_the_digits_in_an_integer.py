# 2.11 (Separating the Digits in an Integer) Write a script that inputs a five-digit integer
# from the user. Separate the number into its individual digits. Print them separated by three
# spaces each. For example, if the user types in the number 42339, the script should print
# 4 2 3 3 9
# Assume that the user enters the correct number of digits. Use both the floor division and
# remainder operations to “pick off” each digit.

number = int(input("Enter a five-digit number: "))
if number > 10000 & number < 99999:
    first_digit = number // 10000
    second_digit = number // 1000 % 10
    third_digit = number // 100 % 10
    fourth_digit = number // 10 % 10
    fifth_digit = number % 10

    print(first_digit, second_digit, third_digit, fourth_digit, fifth_digit)
