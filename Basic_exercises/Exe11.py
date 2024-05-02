"""
Write a Program to extract each digit from an integer in the reverse order.
For example, If the given int is 7536, the output shall be “6 3 5 7“, 
with a space separating the digits.
"""

def reverse_order(n):
    while n > 0:
        print(n % 10, end=' ')
        n = n // 10

n = int(input("Enter a number: "))
reverse_order(n)    

