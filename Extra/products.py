# Given an integer array nums, write a function that returns an array products, such that each
# entry at position i, in products is a product of all other elements in nums except nums[i].
# Example: if nums = [4, 5, 10, 2], your function should return [100, 80, 40, 200]

nums = [4, 5, 10, 2]
products = 1
newArrayOfProducts = []

for num in nums:
    products *= num

for x in nums:
    newArrayOfProducts.append(int(products / x))
print(newArrayOfProducts)