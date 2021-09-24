# 3.9 (Separating the Digits in an Integer) In Exercise 2.11, you wrote a script that separated a
# five-digit integer into its individual digits and displayed them. Reimplement your
# script to use a loop that in each iteration “picks off” one digit (left to right) using the //
# and % operators, then displays that digit.

number = int(input("Enter a five-digit number: "))

if number > 10000 & number < 99999:
    first_digit = number // 10000
    second_digit = number // 1000 % 10
    third_digit = number // 100 % 10
    fourth_digit = number // 10 % 10
    fifth_digit = number % 10

    print(first_digit, second_digit, third_digit, fourth_digit, fifth_digit)

picked_number_list = []
def number_picker():
    for _ in range(6):
        number % 10

