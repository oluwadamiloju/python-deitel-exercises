def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif type(n) != int:
        raise TypeError("Enter an integer")
    else:
        return n * factorial(n - 1)


for i in range(1, 19):
    print(factorial(i), sep='\n')
