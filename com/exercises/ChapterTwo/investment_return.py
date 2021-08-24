principal = 1000
rate = 0.07
number_of_years = 10


def amount():
    return principal * (1 + rate) ** number_of_years


print("Amount at the end of", number_of_years, "is", amount())


number_of_years = 20
print("Amount at the end of", number_of_years, "is", amount())


number_of_years = 30
print("Amount at the end of", number_of_years, "is", amount())
