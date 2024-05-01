"""
Write a program to check if the given number 
is a palindrome number.
"""

def is_palindrome(n):
    num = str(n)
    rev_num = num[::-1]
    return rev_num == num

n = int(input('Enter a number: '))

print(is_palindrome(n))