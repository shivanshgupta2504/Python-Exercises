"""
Write a program to check if the given number 
is a palindrome number.
"""

def is_palindrome(n):
    rev_num = n[::-1]
    return rev_num == n

n = input('Enter a number: ')

print(is_palindrome(n))