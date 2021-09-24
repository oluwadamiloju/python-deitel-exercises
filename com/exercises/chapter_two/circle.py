# 2.5 (Circle Area, Diameter and Circumference) For a circle of radius 2, display the diameter, circumference and area. Use the value 3.14159 for π. Use the following formulas
# (r is the radius): diameter = 2r, circumference = 2πr and area = πr2. [In a later chapter, we’ll
# introduce Python’s math module which contains a higher-precision representation of π.]

radius = 2
pi = 3.14159


def diameter():
    return 2 * radius


def circumference():
    return 2 * pi * radius


def area():
    return pi * radius * radius


print(diameter(), circumference(), area())
