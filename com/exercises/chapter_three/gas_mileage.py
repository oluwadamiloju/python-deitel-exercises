# 3.11 (Miles Per Gallon) Drivers are concerned with the mileage obtained by their automobiles.
# One driver has kept track of several tankfuls of gasoline by recording miles driven
# and gallons used for each tankful. Develop a sentinel-controlled-repetition script that
# prompts the user to input the miles driven and gallons used for each tankful. The script
# should calculate and display the miles per gallon obtained for each tankful.
# After processing all input information, the script should calculate and display the combined miles per
# gallon obtained for all tankfuls (that is, total miles driven divided by total gallons used).

# Enter the gallons used (-1 to end): 12.8
# Enter the miles driven: 287
# The miles/gallon for this tank was 22.421875
# Enter the gallons used (-1 to end): 10.3
# Enter the miles driven: 200
# The miles/gallon for this tank was 19.417475
# Enter the gallons used (-1 to end): 5
# Enter the miles driven: 120
# The miles/gallon for this tank was 24.000000
# Enter the gallons used (-1 to end): -1
# The overall average miles/gallon was 21.601423

count = 0
gallons_used = float(input("Enter the gallons used (-1 to end): "))
miles_driven = float(input("Enter the miles driven: "))
average_mile_per_gallon = 0
total_miles_per_gallon = 0

while gallons_used != -1 and miles_driven != -1:
    count += 1
    miles_per_gallon = miles_driven / gallons_used
    total_miles_per_gallon += miles_per_gallon
    print(f'The miles/gallon for this tank was {miles_per_gallon}')
    average_mile_per_gallon = total_miles_per_gallon / count
    gallons_used = float(input("Enter the gallons used (-1 to end): "))
    miles_driven = float(input("Enter the miles driven: "))
print(f'The overall average miles/gallon was {average_mile_per_gallon}')
