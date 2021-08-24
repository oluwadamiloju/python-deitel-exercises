print("Side 1", "Side2", "Hypotenuse", sep="\t\t\t")

for side1 in range(1, 20):
    for side2 in range(1, 20):
        for hypotenuse in range(1, 20):
            if hypotenuse ** 2 == side1 ** 2 + side2 ** 2:
                print(f"{side1}\t\t\t\t{side2}\t\t\t\t{hypotenuse}")
