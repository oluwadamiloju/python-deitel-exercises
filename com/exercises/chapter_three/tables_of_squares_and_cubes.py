print("number", "square", "cube", sep="\t")

for number in range(6):
    print(f'{number:>6} {number * number:>7} {number * number * number:>5}')
