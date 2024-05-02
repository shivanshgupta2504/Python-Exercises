"""
Write a function called exponent(base, exp) that 
returns an int value of base raises to the power of exp.
"""

def exponent(base, exp):
    return base ** exp


base = int(input("Enter base: "))
exp = int(input("Enter exponent: "))
print(exponent(base, exp))
