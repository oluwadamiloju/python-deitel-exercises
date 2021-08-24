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
