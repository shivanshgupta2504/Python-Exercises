"""
Given two integer numbers, return their product only 
if the product is equal to or lower than 1000. Otherwise, return their sum.
"""

def calculate(a, b):
    """
    return the product only if the product is equal to or lower than 1000. 
    Otherwise, return the sum.
    """
    if a * b <= 1000:
        return a * b
    else:
        return a + b

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(calculate(a, b))
