# 2.10 (Arithmetic, Smallest and Largest) Write a script that inputs three integers from
# the user. Display the sum, average, product, smallest and largest of the numbers. Note that
# each of these is a reduction in functional-style programming.

first_number = int(input("Enter a number: "))
second_number = int(input("Enter a number: "))
third_number = int(input("Enter a number: "))

sum_of_numbers = first_number + second_number + third_number
print("The sum of the numbers is", sum_of_numbers)
average_of_numbers = first_number + second_number + third_number / 3
print("The average of the numbers is", average_of_numbers)
product_of_numbers = first_number * second_number * third_number
print("The product of the numbers is", product_of_numbers)

largest = first_number
if second_number > largest:
    largest = second_number
if third_number > largest:
    largest = third_number
print("The largest of the numbers is", largest)

smallest = first_number
if second_number < smallest:
    smallest = second_number
if third_number < smallest:
    smallest = third_number
print("The smallest of the numbers is", smallest)