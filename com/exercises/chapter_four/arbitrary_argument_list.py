# 4.13 (Arbitrary Argument List) Calculate the product of a series of integers that are passed to the
# function product, which receives an arbitrary argument list. Test your function with several calls,
# each with a different number of arguments.

def product(*args):
    prd = 1
    for value in args:
        prd *= value
    return prd


print(product(1))
print(product(1, 2, 3))
print(product(1, 2, 3, 4))
