# 4.4 (What’s Does This Code Do?) What does the following mystery function do?
# Assume you pass the list [1, 2, 3, 4, 5] as an argument.

def mystery(x):
    y = 0
    for value in x:
        y += value ** 2
    return y


print(mystery([1, 2, 3, 4, 5]))


# code squares each value passed as an argument and adds it to a variable first initialized to zero.