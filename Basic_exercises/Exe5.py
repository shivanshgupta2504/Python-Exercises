"""
Write a function to return True if the first and last number
of a given list is same. 
If numbers are different then return False.
"""

def is_same(numbers):
    if numbers[0] == numbers[-1]:
        return True
    else:
        return False

numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

print(is_same(numbers_x))
print(is_same(numbers_y))
