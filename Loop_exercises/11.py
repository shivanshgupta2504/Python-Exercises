"""
Write a program to calculate the sum of series up to n term. For example, if n = 5 
the series will become 2 + 22 + 222 + 2222 + 22222 = 24690
"""

n = int(input("Enter a number: "))
sum = 0
start = 0

for i in range(1, n+1):
    start = start * 10 + 2
    sum += start

print(f"Sum is {sum}")
