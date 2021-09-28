# 4.9 (Temperature Conversion) Implement a fahrenheit function that returns the Fahrenheit equivalent of
# a Celsius temperature. Use the following formula:
#             F = (9 / 5) * C + 32
# Use this function to print a chart showing the Fahrenheit equivalents of all Celsius temperatures in the
# range 0–100 degrees. Use one digit of precision for the results. Print the outputs in a neat tabular format.

def celsius_to_fahrenheit(celsius):
    return round((9 / 5) * celsius + 32, 1)


print("Celsius (degree C)", "Fahrenheit (F)", sep="\t\t")

for i in range(1, 101):
    print(f'{i:>17} {celsius_to_fahrenheit(i):>19}')
