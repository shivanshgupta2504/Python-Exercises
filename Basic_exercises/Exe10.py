"""
Given two list of numbers, write a program to create 
a new list such that the new list should contain odd numbers 
from the first list and even numbers from the second list.
"""

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

# This is list comprehension
new_list = [x for x in list1 if x % 2 != 0]
new_list.extend([x for x in list2 if x % 2 == 0])

print(new_list)