sum_of_numbers = 0
average_of_numbers = 0
product_of_numbers = 1
smallest = 0
largest = 0
number_list = []

for i in range(4):
    number = int(input("Enter a number: "))
    number_list.append(number)

for num in number_list:
    sum_of_numbers += num
    print(f'The sum of the numbers is {sum_of_numbers}')
    average_of_numbers = sum_of_numbers / 4
    print(f'The average of the numbers is {average_of_numbers}')
    product_of_numbers *= num
    print(f'The product of the numbers is {product_of_numbers}')

largest = max(number_list)
print(f'The largest of the numbers is {largest}')
smallest = min(number_list)
print(f'The smallest of the numbers is {smallest}')
