# 3.13 (Factorials) Factorial calculations are common in probability. The factorial of a
# nonnegative integer n is written n! (pronounced “n factorial”) and is defined as follows:
# n! = n · (n - 1) · (n - 2) · … · 1
# for values of n greater than or equal to 1, with 0! defined to be 1. So,
# 5! = 5 · 4 · 3 · 2 · 1
# which is 120. Factorials increase in size very rapidly. Write a script that inputs a nonnegative integer
# and computes and displays its factorial. Try your script on the integers 10, 20, 30 and even larger
# values. Did you find any integer input for which Python could not produce an integer factorial value?

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
