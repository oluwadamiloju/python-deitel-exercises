# 3.19 (Brute-Force Computing: Pythagorean Triples) A right triangle can have sides that
# are all integers. The set of three integer values for the sides of a right triangle is called a
# Pythagorean triple. These three sides must satisfy the relationship that the sum of the squares
# of two of the sides is equal to the square of the hypotenuse. Find all Pythagorean triples for
# side1, side2 and hypotenuse (such as 3, 4 and 5) all no larger than 20. Use a triple-nested
# for-loop that tries all possibilities. This is an example of “brute-force” computing. You’ll
# learn in more advanced computer science courses that there are many interesting problems for
# which there is no known algorithmic approach other than sheer brute force.

print("Side 1", "Side2", "Hypotenuse", sep="\t\t\t")

for side1 in range(1, 20):
    for side2 in range(1, 20):
        for hypotenuse in range(1, 20):
            if hypotenuse ** 2 == side1 ** 2 + side2 ** 2:
                print(f"{side1}\t\t\t\t{side2}\t\t\t\t{hypotenuse}")
