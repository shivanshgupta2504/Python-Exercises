"""
Iterate the given list of numbers and print only 
those numbers which are divisible by 5
"""

def print5(list):
    for i in list:
        if i % 5 == 0:
            print(i, end=' ')
    print()

list = [10, 20, 33, 46, 55]

print5(list)