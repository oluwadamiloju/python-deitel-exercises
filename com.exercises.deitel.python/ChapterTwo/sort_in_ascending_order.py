first_number = float(input("Enter a floating number: "))
second_number = float(input("Enter a floating number: "))
third_number = float(input("Enter a floating number: "))

smallest = first_number
if second_number < first_number:
    smallest = second_number
    second_number = first_number
    first_number = smallest
if first_number < second_number:
    first_number = smallest
    second_number = second_number
if third_number < first_number:
    smallest = third_number
    third_number = first_number
    first_number = smallest
if third_number < second_number:
    smaller = third_number
    third_number = second_number
    second_number = smaller
if third_number > second_number and third_number > first_number:
    first_number = smallest
    second_number = second_number
    third_number = third_number


print(first_number, second_number, third_number)