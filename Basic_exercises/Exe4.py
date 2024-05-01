"""
Write a program to remove characters from
a string starting from zero up to n and return a new string.
Example:
remove_chars("pynative", 4) so output must be 'tive'
"""

def remove_chars(str, n):
    if n >= len(str):
        return ""
    else:
        return str[n:] 

str = input('Enter a string: ')
n = int(input('Enter letters to be removed: '))

print(remove_chars(str, n))