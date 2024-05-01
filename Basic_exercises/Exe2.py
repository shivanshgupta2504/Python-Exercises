"""
Write a program to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.
"""

def sum(n):
    prev = 0
    for i in range(1, n):
        sum = prev + i
        print(f"Current : {i} Previous : {prev} Sum : {sum}")
        prev = i


n = int(input('Enter a number: '))
sum(n)
