# 2.8 (Table of Squares and Cubes) Write a script that calculates the squares and cubes
# of the numbers from 0 to 5. Print the resulting values in table format, as shown below. Use
# the tab escape sequence to achieve the three-column output.
# number square cube
# 0      0      0
# 1      1      1
# 2      4      8
# 3      9      27
# 4      16     64
# 5      25     125

# The next chapter shows how to “right align” numbers. You could try that as an extra challenge here.
# The output would be:
# number square cube
#      0      0    0
#      1      1    1
#      2      4    8
#      3      9   27
#      4     16   64
#      5     25  125

print("number\t square\t cube")

for number in range(6):
    print(number, number * number, number * number * number, sep="\t\t ")